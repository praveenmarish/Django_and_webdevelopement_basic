//Initiate the timer
function initiator(){
    document.getElementById("count").disabled=true
    var val=document.getElementById("time").value
    run(val)
}
//Add 0's to the begining for better look
function pad(num) {
  if (num<10){
    return "0"+num
  }
  else{
      return num
  }
}
//Start the clock
function run(val){
    document.getElementById("add").disabled=false
    document.getElementById("reduce").disabled=false
    
    x=setInterval(() => {
        var min=parseInt(val/60)
        var sec=val%60
        val -= 1
        document.getElementById("clock").innerHTML=pad(min)+":"+pad(sec)
        if (val<0){
            clearInterval(x)
            document.getElementById("clock").innerHTML='Ended'
            document.getElementById("count").disabled=false
            document.getElementById("add").disabled=true
            document.getElementById("reduce").disabled=true
        }
    }, 1000)
} 
//Add more time to clock
function add(){
    clearInterval(x)
    var val=document.getElementById("clock").innerText
    var sec=val.split(":")[1]
    var min=val.split(":")[0]
    var addedVal=document.getElementById("time").value
    run((parseInt(min)*60)+parseInt(sec)+parseInt(addedVal))
}
//Reduce time from clock
function reduce(){
    clearInterval(x)
    var val=document.getElementById("clock").innerText
    var sec=val.split(":")[1]
    varmin=val.split(":")[0]
    var reduceVal=document.getElementById("time").value
    run((parseInt(min)*60)+parseInt(sec)-parseInt(reduceVal))
}