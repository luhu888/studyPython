function change(ths) {
    var a =document.getElementsByClassName("parent");
    a[0].innerText='变变变！！！';
}
//当js代码中有找标签的操作的时候，别忘了页面加载的时候的顺序，以防出现找不到标签的情况出现，我们可以将这个script标签放到body标签最下面，或者用window.onload，这里我没有放，你们练习的时候放到下面去
    var intervalId; //用来保存定时器对象，因为开始定时器是一个函数，结束定时器是一个函数，两个函数都是操作的一个定时器，让他们互相能够操作这个定时器，就需要一个全局变量来接受一下这个对象
　　
　　
　　//把当前事件放到id为i1的input标签里面
    function f() {
      var timeStr = (new Date()).toLocaleString(); // 1.拿到当前时间
      var inputEle = document.getElementById("i1");// 2.获取input标签对象
      inputEle.value = timeStr;  //3.将事件赋值给input标签的value属性
    }
　　//开始定时任务
    function start() {
      f();
      if (intervalId === undefined) { //如果不加这个判断条件，你每次点击开始按钮，就创建一个定时器，每点一次就创建一个定时器，点的次数多了就会在页面上生成好多个定时器，并且点击停止按钮的时候，只能停止最后一个定时器，这样不好，也不对，所以加一个判断
        intervalId = setInterval(f, 1000);
      }
    }
    //结束定时任务
    function end() {
      clearInterval(intervalId); //　清除对应的那个定时器
      intervalId = undefined;
    }
    function func1() {
        $("#d1")[0].innerText='哈哈蛤';
        // $('#c1')[0].innerText='哈哈蛤';

    }