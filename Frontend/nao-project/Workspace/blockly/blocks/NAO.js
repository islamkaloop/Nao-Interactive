
//Blockly.Constants.Actions.HUE = "#00ace6";

Blockly.defineBlocksWithJsonArray([
  {
    "type": "start",
    "message0": "%{BKY_START}",
    "nextStatement": null,
    "tooltip": "connect Nao",
    "helpUrl": "",
    "style": "start"

  },

  {
    "type": "talk",
     "message0":"%{BKY_TALK}",
     "args0": [{
        "type": "input_value",
        "name": "text",
        "check": "String",
        "align": "CENTRE"
      },
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/talk.png",
        "width": 80,
        "height": 80,
        "style": "action_blocks",

        "alt": "*",
        "flipRtl": false
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "style":"action_blocks",
    "tooltip": "enter a text ",
    "helpUrl": ""
  },
  {
    "type": "wave",
    "message0": "%{BKY_WAVE}",
    "args0": [
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/wave.png",
        "width": 80,
        "height": 80,
        "alt": "*",
        "flipRtl": false
      }],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make nao wave his hand",
    "helpUrl": ""
  },
  {
    "type": "wipe",
    "message0":"%{BKY_WIPE}",
    "args0": [
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/wipe.png",
        "width": 80,
        "height": 80,
        "alt": "stand",
        "flipRtl": false
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make nao wipe his forehead",
    "helpUrl": ""
  },
  {
    "type": "stand",
    "message0":"%{BKY_STAND}",
    "args0": [
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/standing.png",
        "width": 80,
        "height": 80,
        "alt": "stand",
        "flipRtl": false
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make Nao stand",
    "helpUrl": ""
  },
  {
    "type": "sit",
    "message0": "%{BKY_SIT}",
    "args0": [
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/sit.png",
        "width": 80,
        "height": 80,
        "alt": "stand",
        "flipRtl": false
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make Nao sit",
    "helpUrl": ""
  },
  {
    "type": "crouch",
    "message0": "%{BKY_CROUCH}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make Nao crouch",
    "helpUrl": ""
  },
  {
    "type": "Lying_Belly",
    "message0": "%{BKY_LYING_BELLY}",
    "args0": [
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/on stomach.png",
        "width": 80,
        "height": 80,
        "alt": "stand",
        "flipRtl": false
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make Nao lie on his belly",
    "helpUrl": ""
  },
  {
    "type": "Lying_Back",
    "message0": "%{BKY_LYING_BACK}",
    "args0": [
      {
        "type": "field_image",
        "src": "../Workspace/blockly/Nao images/lay down.png",
        "width": 80,
        "height": 80,
        "alt": "stand",
        "flipRtl": false
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "make Nao lie on his back",
    "helpUrl": ""
  },
  {
    "type": "walk",
    "message0": "%{BKY_WALK}",
    "args0": [
      
      {
        "type": "field_dropdown",
        "name": "direction",
        "options": [
          [
            "%{BKY_FORWARD}",
            "%{BKY_FORWARD}"
          ],
          [
            "%{BKY_BACKWARD}",
            "%{BKY_BACKWARD}"
          ]
        ]
      },
      {
        "type": "input_value",
        "name": "distance",
        "check": "Number"
      },
        {
          "type": "field_image",
          "src": "../Workspace/blockly/Nao images/walk .png",
          "width": 80,
          "height": 80,
          "alt": "stand",
          "flipRtl": false
        }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "turn",
    "message0": "%{BKY_TURN}",
    "args0": [
      {
        "type": "field_angle",
        "name": "angle",
        "angle": 90
      },
      {
        "type": "field_dropdown",
        "name": "direction",
        "options": [
          [
            "%{BKY_LEFT}",
            "%{BKY_LEFT}"
          ],
          [
            "%{BKY_RIGHT}",
            "%{BKY_RIGHT}"
          ]
        ]
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },

{
  "type": "open_hand",
  "message0": "%{BKY_OPEN_HAND}",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "LR",
      "options": [
        [
          "%{BKY_LEFT}",
          "%{BKY_LEFT}"
        ],
        [
          "%{BKY_RIGHT}",
          "%{BKY_RIGHT}"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "style": "action_blocks",
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "close_hand",
  "message0": "%{BKY_CLOSE_HAND}",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "LR",
      "options": [
        [
          "%{BKY_LEFT}",
          "%{BKY_LEFT}"
        ],
        [
          "%{BKY_RIGHT}",
          "%{BKY_RIGHT}"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "style": "action_blocks",
  "tooltip": "",
  "helpUrl": ""
},

{
    "type": "blink",
    "message0": "%{BKY_BLINK}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },

  {
    "type":"taichi",
    "message0": "%{BKY_TAICHI}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type":"Macarena",
    "message0": "%{BKY_MACARENA}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type":"Pushups",
    "message0": "%{BKY_PUSHUPS}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type":"Blow_kiss",
    "message0": "%{BKY_BLOW_KISS}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type":"Bow",
    "message0": "%{BKY_BOW}",
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "random_eyes",
    "message0":"%{BKY_RANDOM_EYES}",
    "args0": [
      {
        "type": "field_number",
        "name": "time",
        "value": 0
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "rasta",
    "message0": "%{BKY_RASTA}",
    "args0": [
      {
        "type": "field_number",
        "name": "time",
        "value": 0
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "style": "action_blocks",
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "set_color",
    "message0": "%{BKY_SET_COLOR}",
    "args0": [
      {
        "type": "field_colour",
        "name": "NAME",
        "colour": "#ff0000"
      },
      {
        "type": "field_dropdown",
        "name": "Leds",
        "options": [
          [
            "eyes",
            "FaceLeds"
          ],
          [
            "left eyes",
            "LeftFaceLeds"
          ],
          [
            "right eyes",
            "RightFaceLeds"
          ],
          [
            "left foot",
            "LeftFootLeds"
          ],
          [
            "right foot",
            "RightFootLeds"
          ]
        ]
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 270,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "head_sensor",
    "message0": "%{BKY_HEAD_SENSOR}",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "Head",
        "options": [
          [
            "Front",
            "Front"
          ],
          [
            "Middle",
            "Middle"
          ],
          [
            "Back",
            "Back"
          ]
        ]
      }
    ],
    "inputsInline": true,
    "output": null,
    "colour": 180,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "hand_sensor",
    "message0": "%{BKY_HAND_SENSOR}",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "Hand",
        "options": [
          [
            "Left",
            "Left"
          ],
          [
            "Right",
            "Right"
          ],
        ]
      }
    ],
    "inputsInline": true,
    "output": null,
    "colour": 180,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "bumper_sensor",
    "message0": "%{BKY_BUMPER_SENSOR}",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "Bumper",
        "options": [
          [
            "Left",
            "Left"
          ],
          [
            "Right",
            "Right"
          ],
        ]
      }
    ],
    "inputsInline": true,
    "output": null,
    "colour": 180,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "ultrasonic_sensor",
    "message0": "%{BKY_ULTRASONIC}",
    "output": null,
    "colour": 180,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "voice_reco",
    "message0": "%{BKY_SPEECH}",
    "previousStatement": null,
    "nextStatement": null,
    "colour": 290,
    "tooltip": "Order NAO with Voice",
    "helpUrl": ""
  },
  {
    "type": "seq_voice_reco",
    "message0": "%{BKY_SEQSPEECH}",
    "previousStatement": null,
    "nextStatement": null,
    "colour": 290,
    "tooltip": "Order NAO with Voice",
    "helpUrl": ""
  }
  
  ]);
  