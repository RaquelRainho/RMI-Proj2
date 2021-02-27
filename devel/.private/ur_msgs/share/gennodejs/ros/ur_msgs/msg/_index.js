
"use strict";

let MasterboardDataMsg = require('./MasterboardDataMsg.js');
let RobotModeDataMsg = require('./RobotModeDataMsg.js');
let ToolDataMsg = require('./ToolDataMsg.js');
let RobotStateRTMsg = require('./RobotStateRTMsg.js');
let Digital = require('./Digital.js');
let IOStates = require('./IOStates.js');
let Analog = require('./Analog.js');

module.exports = {
  MasterboardDataMsg: MasterboardDataMsg,
  RobotModeDataMsg: RobotModeDataMsg,
  ToolDataMsg: ToolDataMsg,
  RobotStateRTMsg: RobotStateRTMsg,
  Digital: Digital,
  IOStates: IOStates,
  Analog: Analog,
};
