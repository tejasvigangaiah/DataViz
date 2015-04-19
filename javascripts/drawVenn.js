/**
 * Created by kpbhatt on 3/15/2015.
 */
var tooltip;

var cuisines = "";

function startDrawingVenn() {
    if (tooltip !=  null)
        tooltip.remove();

    var chart = venn.VennDiagram()
        .width(1000)
        .height(1000);

    var div = d3.select("#venn")
    div.datum(sets).call(chart);

    tooltip = d3.select("body").append("div")
        .attr("class", "venntooltip");

    div.selectAll("path")
        .style("stroke-opacity", 0)
        .style("stroke", "#fff")
        .style("stroke-width", 0);

    div.selectAll("g")
        .on("mouseover", function (d, i) {
            // sort all the areas relative to the current item
            venn.sortAreas(div, d);

            var tempStr = "";
            for (var i = 0; i < d.sets.length; i++) {
                var index = d.sets[i];
                tempStr += foodJson[index].label + " & "
            }
            tempStr = tempStr.substring(0, tempStr.length - 2);

            // Display a tooltip with the current size
            tooltip.transition().duration(400).style("opacity", .9);
            tooltip.text(tempStr);

            // highlight the current path
            var selection = d3.select(this).transition("tooltip").duration(400);
            selection.select("path")
                .style("stroke-width", 3)
                .style("fill-opacity", d.sets.length == 1 ? .4 : .1)
                .style("stroke-opacity", 1);
        })

        .on("mousemove", function () {
            tooltip.style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })

        .on("mouseout", function (d, i) {
            tooltip.transition().duration(400).style("opacity", 0);
            var selection = d3.select(this).transition("tooltip").duration(400);
            selection.select("path")
                .style("stroke-width", 0)
                .style("fill-opacity", d.sets.length == 1 ? .25 : .0)
                .style("stroke-opacity", 0);
        })
        .on("click", function (d, i) {
            cuisines = "";
            venn.sortAreas(div, d);
            for (var i = 0; i < d.sets.length; i++) {
                var index = d.sets[i];
                cuisines += foodJson[index].label + ","
            }
            cuisines = cuisines.substring(0, cuisines.length - 1);

            getRestaurantList(cuisines);
        });

}
