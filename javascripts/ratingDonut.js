/**
 * Created by kpbhatt on 4/15/2015.
 */
var star1 = 5;
var star2 = 4;
var star3 = 3;
var star4 = 2;
var star5 = 1;
//donutRating(star1, star2, star3, star4, star5);

function donutRating(star1, star2, star3, star4, star5) {
    var average_aces = c3.generate({
        bindto: '#donut2',
        data: {
            columns: [
                ['5 Star', star5],
                ['4 Star', star4],
                ['3 Star', star3],
                ['2 Star', star2],
                ['1 Star', star1]
            ],
            type: 'donut',
            colors: {
                5: '#04B404',
                4: '#1E90FF',
                3: '#00FFFF',
                2: '#FFA500',
                1: '#FF0000'
            }
        },
        size: {
            height: 250
        },
        donut: {
            title: 'Number of Stars',
            label: {
                format: function (value, ratio, id) {
                    return d3.format('')(value);
                }
            }
        }
    });
}