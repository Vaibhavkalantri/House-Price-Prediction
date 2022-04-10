
const hi = () => {
    console.log("hi");
  }
document.getElementById("submit").addEventListener('click',hi );

document.getElementById('HpData').addEventListener('submit', (e) => {
    e.preventDefault();
    var elements = document.getElementById("HpData").elements;
    var obj ={};
    for(var i = 0 ; i < elements.length ; i++){
        var item = elements.item(i);
        obj[item.name] = item.value;
    }
    console.log(obj)
    
  });

var MenuItems = document.getElementById("MenuItems");
MenuItems.style.maxHeight = "0px";
function menutoggle() {
  if (MenuItems.style.maxHeight == "0px") {
    MenuItems.style.maxHeight = "200px";
  } else {
    MenuItems.style.maxHeight = "0px";
  }
}
