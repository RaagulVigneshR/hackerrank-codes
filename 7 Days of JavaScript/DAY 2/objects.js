function printObjectProperty(myObject) {
  console.log(myObject)
}
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    var obj = _input.split(' ');
    var myObject = new Object;
    myObject.type = "Fiat";
    myObject.model = "500";
    myObject.color = "White";

    printObjectProperty(myObject);
});
