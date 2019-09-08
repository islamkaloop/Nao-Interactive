function CMBS() {
    return {
        "loop_blocks": {
            "colourPrimary": "#4a148c",
            "colourSecondary": "#AD7BE9",
            "colourTertiary": "#CDB6E9"
        }
    };
}

function themeSettings(){
    var theme = new Blockly.Theme(CMBS());
    Blockly.setTheme(theme); 
}

function test(){
    var theme = new Blockly.Theme(CMBS());
    Blockly.setTheme(theme);}