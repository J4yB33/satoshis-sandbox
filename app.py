from flask import Flask, render_template_string
import requests
app = Flask(__name__)
C = {"bg":"#0d1117","cd":"#161b22","br":"#30363d","pu":"#a331fb","cy":"#00d4ff","rd":"#ff5555","tx":"#e6edf3","mu":"#8b949e","gr":"#238636"}
T = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
body{background:{{c.bg}};color:{{c.tx}};font-family:sans-serif;padding:20px;display:flex;justify-content:center}
.con{background:{{c.cd}};border:1px solid {{c.br}};padding:2rem;border-radius:15px;width:100%;max-width:650px;box-shadow:0 10px 30px rgba(0,0,0,0.5)}
h1{color:{{c.cy}};margin:0 0 20px 0;font-size:1.8rem}.tic{background:rgba(163,49,251,0.1);border-left:4px solid {{c.pu}};padding:12px;margin-bottom:20px;font-weight:bold;display:flex;justify-content:space-between;align-items:center}
textarea{width:100%;height:100px;background:{{c.bg}};border:1px solid {{c.br}};color:#fff;border-radius:8px;padding:12px;box-sizing:border-box;outline:none;font-family:monospace}
.btn-g{margin-top:15px;display:flex;gap:10px}.btn{border:none;padding:12px 24px;border-radius:6px;cursor:pointer;font-weight:bold;transition:0.3s}
.b-ch{background:{{c.cy}};color:#000}.b-cl{background:{{c.rd}};color:#fff}.b-curr{background:#21262d;color:{{c.cy}};border:1px solid {{c.br}};padding:5px 10px;font-size:0.8rem}
.card{background:{{c.bg}};border:1px solid {{c.br}};border-radius:12px;padding:20px;margin-top:20px;position:relative}
.tag{background:#21262d;color:{{c.mu}};padding:2px 8px;border-radius:4px;font-size:0.7rem;text-transform:uppercase;margin-bottom:10px;display:inline-block}
.btc{font-size:1.6rem;font-weight:bold;color:#fff}.cur-v{color:{{c.mu}};font-size:1.2rem}.sats{font-size:0.9rem;color:{{c.mu}};margin-bottom:15px}
.tx-item{display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(255,255,255,0.03);font-size:0.8rem}
.tx-in{color:{{c.gr}}}.tx-out{color:{{c.rd}}}
.port{margin-top:25px;padding:25px;border:1px dashed {{c.cy}};border-radius:12px;text-align:center}
.t-val{font-size:2rem;font-weight:bold;color:{{c.cy}};display:block}
.ref-btn{position:absolute;top:20px;right:20px;background:#21262d;color:{{c.cy}};border:1px solid {{c.br}};padding:5px 10px;border-radius:6px;font-size:0.75rem;cursor:pointer}
</style></head><body><div class="con"><h1>Satoshi’s Sandbox</h1>
<div class="tic"><span id="tp">Price: Fetching...</span><button class="btn b-curr" onclick="toggleCurr()" id="currBtn">Currency: USD</button></div>
<textarea id="ad" placeholder="Enter addresses..."></textarea><div class="btn-g">
<button class="btn b-ch" onclick="go()">Check Balance</button>
<button class="btn b-cl" onclick="clearAll()">Clear All</button>
</div><div id="res"></div><div id="pa"></div></div><script>
let prU=0,prG=0,curr='USD';
async function getP(){
    try{
        const r=await fetch('https://api.coindesk.com/v1/bpi/currentprice.json');
        const d=await r.json(); prU=d.bpi.USD.rate_float; prG=d.bpi.GBP.rate_float;
    }catch(e){
        try{
            const rb=await fetch('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT');
            const db=await rb.json(); prU=parseFloat(db.price); prG=prU * 0.79;
        }catch(e2){ console.log("Price fetch fail"); }
    }
    updatePriceDisplay();
}
function updatePriceDisplay(){
    let p = curr==='USD' ? prU : prG; let s = curr==='USD' ? '$' : '£';
    document.getElementById('tp').innerText='Price: '+s+p.toLocaleString(undefined,{minimumFractionDigits:2});
}
function toggleCurr(){ curr = curr==='USD' ? 'GBP' : 'USD'; document.getElementById('currBtn').innerText='Currency: '+curr; updatePriceDisplay(); if(document.getElementById('ad').value.length > 5) go(); }
function fD(u){return u?new Date(u).toLocaleDateString('en-GB'):'N/A'}
function clearAll(){ localStorage.removeItem('btc_addresses'); document.getElementById('res').innerHTML=''; document.getElementById('ad').value=''; document.getElementById('pa').innerHTML=''; }

async function go(singleAddr=null){
    const i=singleAddr || document.getElementById('ad').value; 
    const adds=i.split(/[\\s,\\n,]+/).filter(a=>a.length>5);
    if(adds.length===0) return;
    if(!singleAddr) { document.getElementById('res').innerHTML='Syncing...'; localStorage.setItem('btc_addresses', JSON.stringify(adds)); }

    let tB=0,h='',p=curr==='USD'?prU:prG,s=curr==='USD'?'$':'£';
    for(const a of adds){
        try{
            const r=await fetch(`https://api.blockcypher.com/v1/btc/main/addrs/${a}?limit=5`);
            const d=await r.json();
            if(d.error) throw new Error(d.error);
            const b=d.final_balance/1e8; tB+=b;
            let txH = '<div style="margin-top:10px; border-top:1px solid #30363d; padding-top:10px;"><strong>History:</strong>';
            if(d.txrefs){
                d.txrefs.slice(0,5).forEach(tx => {
                    const type = tx.tx_input_n < 0 ? 'IN' : 'OUT';
                    txH+=`<div class="tx-item"><span class="${type=='IN'?'tx-in':'tx-out'}">${type}</span><span>${(tx.value/1e8).toFixed(8)} BTC</span><span>${fD(tx.confirmed)}</span></div>`;
                });
            }
            let cardHtml = `<div class="card" id="card-${a}"><span class="tag">Address</span><button class="ref-btn" onclick="go('${a}')">Refresh</button><div style="font-family:monospace;font-size:0.85rem;word-break:break-all">${a}</div>
            <div class="btc">${b.toFixed(8)} BTC <span class="cur-v">${s}${(b*p).toLocaleString(undefined,{minimumFractionDigits:2})}</span></div>
            <div class="sats">(${(d.final_balance).toLocaleString()} sats)</div>${txH}</div><div style="background:rgba(35,134,54,0.1);border:1px solid #238636;padding:8px;color:#238636;font-size:0.75rem;border-radius:0 0 12px 12px">Verified on Blockchain</div></div>`;
            if(singleAddr){ document.getElementById('card-'+a).outerHTML = cardHtml; } else { h+=cardHtml; }
        }catch(e){ if(!singleAddr) h+='<div class="card" style="border-color:#ff5555">Sync Error: Check Address or API Limits</div>'; }
    }
    if(!singleAddr) document.getElementById('res').innerHTML=h;
    document.getElementById('pa').innerHTML=`<div class="port"><h3>Live Portfolio Value</h3><span class="t-val">${s}${(tB*p).toLocaleString(undefined,{minimumFractionDigits:2})}</span><span>${tB.toFixed(8)} BTC</span></div>`;
}
getP(); setInterval(getP, 60000); window.onload = () => { const s = localStorage.getItem('btc_addresses'); if(s){ document.getElementById('ad').value = JSON.parse(s).join('\\n'); go(); } };
</script></body></html>"""
@app.route('/')
def i(): return render_template_string(T,c=C)
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
