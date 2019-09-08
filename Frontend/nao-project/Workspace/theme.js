function CMBS() {
    return {
        "logic_blocks": {
            "colourPrimary": "#006666",
            "colourSecondary": "#AD7BE9",
            "colourTertiary": "#CDB6E9"
        },
        "loop_blocks": {
            "colourPrimary": "#ff0080",           
            "colourSecondary": "#64C7FF",
            "colourTertiary": "#C5EAFF"
        },
        "text_blocks": {
            "colourPrimary": "#660033",
            "colourSecondary": "#64C7FF",
            "colourTertiary": "#C5EAFF"
        },
        "math_blocks": {
            "colourPrimary": "#a3c2c2",
            "colourSecondary": "#64C7FF",
            "colourTertiary": "#C5EAFF"
        },
        "action_blocks":{
            "colourPrimary": "#00adbc",
            "colourSecondary": "#64C7FF",
            "colourTertiary": "#C5EAFF"
        },
        "start":{
            "colourPrimary": "#ffad33",
            "colourSecondary": "#64C7FF",
            "colourTertiary": "#C5EAFF"
        }
    };
}

function themeSettings(){
    var theme = new Blockly.Theme(CMBS());
    Blockly.setTheme(theme); 
}