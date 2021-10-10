
const mydata = JSON.parse(document.getElementById('mydata').textContent);
const obj =JSON.parse(mydata);
$(document).ready(function(){

    $.each( obj, function( key, value ) {
        alert( key + ": " + value );
      });
  }); 


for(x in obj)
{
    replace_location(x,"GBD-S01A")
    replace_location(x,"GBD-S02A")
    replace_location(x,"GBD-S03A")
    replace_location(x,"GBD-S04A")
    replace_location(x,"GBD-S05A")
    replace_location(x,"GBD-S06A")
    replace_location(x,"GBD-S07A")
    replace_location(x,"GBD-S08A")
    replace_location(x,"GBD-S09A")
    replace_location(x,"GBD-S10A")
    replace_location(x,"GBD-S11A")
    replace_location(x,"GBD-S12A")
    replace_location(x,"GBD-S13A")
    replace_location(x,"GBD-S14A")
    replace_location(x,"GBD-S01B")
    replace_location(x,"GBD-S02B")
    replace_location(x,"GBD-S03B")
    replace_location(x,"GBD-S04B")
    replace_location(x,"GBD-S05B")
    replace_location(x,"GBD-S06B")
    replace_location(x,"GBD-S07B")
    replace_location(x,"GBD-S08B")
    replace_location(x,"GBD-S09B")
    replace_location(x,"GBD-S10B")
    replace_location(x,"GBD-S11B")
    replace_location(x,"GBD-S12B")
    replace_location(x,"GBD-S13B")
    replace_location(x,"GBD-S14B")
    replace_location(x,"GBD-S01C")
    replace_location(x,"GBD-S02C")
    replace_location(x,"GBD-S03C")
    replace_location(x,"GBD-S04C")
    replace_location(x,"GBD-S05C")
    replace_location(x,"GBD-S06C")
    replace_location(x,"GBD-S07C")
    replace_location(x,"GBD-S08C")
    replace_location(x,"GBD-S09C")
    replace_location(x,"GBD-S10C")
    replace_location(x,"GBD-S11C")
    replace_location(x,"GBD-S12C")
    replace_location(x,"GBD-S13C")
    replace_location(x,"GBD-S14C")

}


function replace_location(x,y)
{
    if(obj[x].fields.location==y)
    {        
        document.getElementById(y).classList.add(obj[x].fields.status);
        return document.getElementById(y).value=obj[x].pk;
    }
    else
    {
        return 0;
    }
    
};

function remove_class(x)
{
    document.getElementById(x).classList.remove("PS")
    document.getElementById(x).classList.remove("ER")
    document.getElementById(x).classList.remove("CM")
    document.getElementById(x).classList.remove("RSS")
    document.getElementById(x).classList.remove("OPS")

    document.getElementById(x).classList.remove("ASA")
    document.getElementById(x).classList.remove("MSO")
    document.getElementById(x).classList.remove("DOWN")
}
