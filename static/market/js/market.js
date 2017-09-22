$(document).ready(function(){
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbtn = document.getElementById("showsortbtn")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"


    alltypebtn.addEventListener("click", function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)
    showsortbtn.addEventListener("click", function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click", function(){
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click", function(){
        sortdiv.style.display = "none"
    },false)

//xiu gai huangkuai
    var lis = document.getElementsByClassName("my")
    for (var i = 0; i < lis.length; i++){
        li = lis[i]
        li.addEventListener("click", function(){
            pid = this.getAttribute("pa")
            console.log(pid)
            document.getElementById(pid).style.display = "block"
        })
    }



    //修改购物车
    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")

    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]
        addShopping.addEventListener("click", function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/0/",{"productid":pid}, function(data){
                if (data.status == "success"){
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                } else {
                    if (data.data == -1){
                        window.location.href = "http://"+window.location.hostname+":"+window.location.port+"/login/"
                    }
                }
            })
        })
    }


    for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]
        subShopping.addEventListener("click", function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/1/",{"productid":pid}, function(data){
                if (data.status == "success"){
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                } else {
                    if (data.data == -1){
                        window.location.href = "http://"+window.location.hostname+":"+window.location.port+"/login/"
                    }
                }
            })
        })
    }

})