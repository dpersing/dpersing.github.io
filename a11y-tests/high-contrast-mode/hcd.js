function HCTest() {
var objDiv, strColor, objFlag;

//reference to img element used to check if images are disabled
objFlag = document.getElementById('flag');

//Create a test div
objDiv = document.createElement('div');

//Set its color style to something unusual
objDiv.style.color = 'rgb(31,41,59)';

//Attach to body so we can inspect it
document.body.appendChild(objDiv);

//Use standard means if available, otherwise use the IE methods
strColor = document.defaultView?document.defaultView.getComputedStyle(objDiv, null).color : objDiv.currentStyle.color;

//Delete the test DIV
document.body.removeChild(objDiv);

//Check if we got back what we set (strColor== ??) If not we are in high contrast mode
// Use .offsetwidth and .readyState (for IE) to check if images are enabled
//If either images are disabled or high contrast is enabled (or both) the CSS stylesheet link will not be added to the page and the visually hidden text will be displayed in place of the missing background image

if (((objFlag.offsetWidth === 1 && objFlag.readyState === 'complete')||(objFlag.offsetWidth === 1 && objFlag.readyState === undefined))
&& (strColor === 'rgb(31,41,59)' || strColor === 'rgb(31, 41, 59)'))
{
var objHead = document.getElementsByTagName('head');
var objCSS = objHead[0].appendChild(document.createElement('link'));
objCSS.rel = 'stylesheet';
objCSS.href = 'alt.css';
objCSS.type = 'text/css';
}
}