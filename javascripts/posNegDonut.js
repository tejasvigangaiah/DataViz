/**
 * Created by kpbhatt on 4/15/2015.
 */

var posVal = 50;
var negVal = 50;
//donutPosNeg(posVal, negVal);
function donutPosNeg(posVal, negVal) {
    var average_aces = c3.generate({
        bindto: '#donut1',
        data: {
            columns: [
                ['Positive', posVal],
                ['Negative', negVal]
            ],
            type: 'donut'

        },
        size: {
            height: 333
        },
        donut: {
            title: 'Reviews'
        }
    });
}