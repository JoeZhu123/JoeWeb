var i = 1;
function autoChangeImage(i){                //自动改变图片
        setTimeout("changeImage(i++); ", 1500);
        setTimeout("back(i); ", 1000);
        setTimeout("autoChangeImage(i = (i%5)); ", 1500);
}
function changeImage(idNum){
        document.getElementById("radio" + idNum).checked = "checked";
        switch(idNum){
            case 0:
                document.getElementById("imgIndex").style.backgroundImage = "url(images/0.jpg)";//改变首页图片
                break;
            case 1:
                document.getElementById("imgIndex").style.backgroundImage = "url(images/1.jpeg)";
                break;
            case 2:
                document.getElementById("imgIndex").style.backgroundImage = "url(images/2.jpeg)";
                break;
            case 3:
                document.getElementById("imgIndex").style.backgroundImage = "url(images/3.jpeg)";
                break;
            case 4:
                document.getElementById("imgIndex").style.backgroundImage = "url(images/4.jpeg)";
                break;
        }
}