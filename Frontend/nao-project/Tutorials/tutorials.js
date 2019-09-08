function count1(){
    var count = 4
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var blocksTypeArray = getAllBlocks_Tut1();
    var p = document.getElementById("count");
    p.innerHTML="Count: "+ blocksTypeArray.length + "/"+ count;
}

function getAllBlocks_Tut1(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        if(!(blocks[i].type == "text" || blocks[i].type == "math_number")){
        blocksTypeArray.push(blocks[i].type);
        }
    }
    return blocksTypeArray;
}
function check1(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","talk","walk","sit"];
    var blocksTypeArray = getAllBlocks_Tut1();

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}

function count2(){
    var count = 4
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var blocksTypeArray = getAllBlocks_Tut1();
    var p = document.getElementById("count");
    p.innerHTML="Count: "+ blocksTypeArray.length + "/"+ count;
}

function getAllBlocks_Tut2(){
    var blocks = Blockly.mainWorkspace.getAllBlocks_Tut2();
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        if(!(blocks[i].type == "text" )){
        blocksTypeArray.push(blocks[i].type);
        }
    }
    return blocksTypeArray;
}

function check2(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","stand","talk","Lying_Back","Lying_Belly","stand"];
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        blocksTypeArray.push(blocks[i].type);
    }

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}
function check3(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","stand","controls_if","head_sensor","Lying_Belly","stand"];
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        blocksTypeArray.push(blocks[i].type);
    }

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}
function check4(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","stand","wave","controls_ifelse","head_sensor","Lying_Belly","Lying_Back","stand"];
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        blocksTypeArray.push(blocks[i].type);
    }

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}


function check5(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","turn","walk","math_number","walk","math_number","walk","math_number"];
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        blocksTypeArray.push(blocks[i].type);
    }

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}
function check6(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","turn","controls_repeat_ext","math_number","walk","math_number"];
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        blocksTypeArray.push(blocks[i].type);
    }

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}
function check7(){
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var correctPathArray = ["start","","controls_repeat_ext","math_number","wipe","math_number"];
    var blocksTypeArray = new Array();
    for (var i = 0; i < blocks.length; i++) {
        blocksTypeArray.push(blocks[i].type);
    }

    console.log(correctPathArray);
    console.log(blocksTypeArray);
    if(correctPathArray.length == blocksTypeArray.length){
        for(var i=0;i<blocksTypeArray.length;i++){
            if(correctPathArray[i]!==blocksTypeArray[i]){
                return false;
            }
        }
    }else{
        return false;
    }

    return true;
}