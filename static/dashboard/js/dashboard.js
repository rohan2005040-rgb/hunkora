const ctx = document.getElementById("salesChart");

if(ctx){

new Chart(ctx,{

type:"line",

data:{

labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

datasets:[{

label:"Sales",

data:[120000,180000,160000,250000,220000,310000,360000],

borderColor:"#ff7a00",

backgroundColor:"rgba(255,122,0,.12)",

fill:true,

tension:.45,

pointRadius:6,

pointHoverRadius:8,

pointBackgroundColor:"#ff7a00",

pointBorderWidth:3,

pointBorderColor:"#fff"

}]

},

options:{

responsive:true,

maintainAspectRatio:false,

plugins:{

legend:{

display:false

}

},

interaction:{

intersect:false,

mode:"index"

},

scales:{

x:{

grid:{

display:false

}

},

y:{

beginAtZero:true,

ticks:{

callback:function(value){

return "৳"+value/1000+"k";

}

}

}

}

}

});

}