var foodJson = [
    {sets: [0], label:"Bars", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [1], label:"Irish", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [2], label:"Chinese", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [3], label:"Italian", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [4], label:"Fast Food", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [5], label:"Pizza", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [6], label:"German", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [7], label:"Indian", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [8], label:"Mexican", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [9], label:"Thai", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [10], label:"French", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [11], label:"Arabian", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [12], label:"Burgers", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [13], label:"Sandwiches", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [14], label:"Vegan", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [15], label:"Bakeries", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [16], label:"Japanese", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [17], label:"Nightlife", initX: 0, initY: 0, size: 3000, color: "#fff"},
    {sets: [18], label:"Coffee & Tea", initX: 0, initY: 0, size: 3000, color: "#fff"}];

var w = window.innerWidth*0.68*0.95;
var h = 562;
var bubbleHeight = 150;
var chosenCount = 0;
var slots = [-1,-1,-1,-1];
var indexAttributes = parseURLParams(window.location.href);;

var svgContainer = d3.select("#svg-container")
    .style("height", h+"px");

var svg = d3.select("#svg-container").append("svg")
    .attr("class", "mainBubbleSVG")
    .attr("width", w)
    .attr("height",h);

var bubbleSplitLine = svg.append("line")
    .attr("x1",0)
    .attr("y1",bubbleHeight)
    .attr("x2",950)
    .attr("y2",bubbleHeight)
    .style("stroke", "red")
    .style("stroke-width", 1);

svg.append("text")
    .attr("x", 55)
    .attr("y", 175)
    .style("font-size", 20)
    .style("text-decoration","underline")
    .text("Select");

svg.append("text")
    .attr("x", 47)
    .attr("y", 195)
    .style("font-size", 20)
    .style("text-decoration","underline")
    .text("Location");

svg.append("text")
    .attr("x", 820)
    .attr("y", 175)
    .style("font-size", 20)
    .style("text-decoration","underline")
    .text("Selected");

svg.append("text")
    .attr("x", 812)
    .attr("y", 195)
    .style("font-size", 20)
    .style("text-decoration","underline")
    .text("Categories");

var drag = d3.behavior.drag()
    .on("drag", dragmove)
    .on("dragstart", dragstart)
    .on("dragend", dragend);

drawBubbles(foodJson);

function drawBubbles(data) {
    var bubbleObj = svg.selectAll(".topBubble")
        .data(data)
        .enter().append("g")
        .attr("id", function(d,i) {return "topBubbleAndText_" + i})
        .call(drag);

    nTop = foodJson.length + sets.length;
    oR = 32;

    var colVals = d3.scale.category20();

    bubbleObj.append("circle")
        .attr("class", "topBubble")
        .attr("id", function(d,i) {return "topBubble" + i;})
        .attr("r", function(d) { return oR; })
        .attr("cx", function(d, i) {d.initX = getCx(d,i); return d.initX;})
        .attr("cy", function (d, i) {d.initY = getCy(d,i); return d.initY})
        .style("fill", function(d,i) {d.color = colVals(i); return d.color;}) // #1f77b4
        .style("opacity",0.7);


    bubbleObj.append("text")
        .attr("class", "topBubbleText")
        .attr("x", function(d, i) {return getCx(d,i);})
        .attr("y", function (d, i) {return getCy(d,i);})
        .style("fill", "black")//function(d,i) {d.color = colVals(i); return d.color;}) // #1f77b4
        .attr("font-size", 10)
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "middle")
        .attr("alignment-baseline", "middle")
        .text(function(d) {return d.label});
}

function printJSONS() {
    for (var i = 0; i < sets.length; i++)
        console.log(sets[i]);
    console.log("========>");
    for (var i = 0; i < foodJson.length; i++)
        console.log(foodJson[i]);
}

var pageX = 0, pageY = 0;
var isDragInProgress = false;
var startX = 0, startY = 0;

function dragstart(d) {
    isDragInProgress = true;
     startX = Number(d3.select(this).selectAll("circle")[0][0].attributes.cx.value);
    startY = Number(d3.select(this).selectAll("circle")[0][0].attributes.cy.value);
}

function dragmove(d) {

    var newX = Number(d3.select(this).selectAll("circle")[0][0].attributes.cx.value) + d3.event.dx;
    var newY = Number(d3.select(this).selectAll("circle")[0][0].attributes.cy.value) + d3.event.dy;

    d3.select(this).selectAll("circle")[0][0].attributes.cx.value = newX;
    d3.select(this).selectAll("circle")[0][0].attributes.cy.value = newY;
    d3.select(this).selectAll("text")[0][0].attributes.x.value = newX;
    d3.select(this).selectAll("text")[0][0].attributes.y.value = newY;

    pageX = d3.mouse(this)[0];
    pageY = d3.mouse(this)[1];
}

function dragend(d) {

    if (pageX > 0 && pageY > bubbleHeight && pageX < w && pageY < h) {
        var index = indexOfFoodArray(d);
        if (index >= 0) {
            if (chosenCount == 4) {
                d3.select(this).selectAll("circle").transition()
                    .attr("cx", d.initX)
                    .attr("cy", d.initY)
                    .duration(400);
                d3.select(this).selectAll("text").transition()
                    .attr("x", d.initX)
                    .attr("y", d.initY)
                    .duration(400);
            } else {
                foodJson.splice(index, 1);
                isDragInProgress = false;
                var indexEmpty = -1;
                d3.select(this).selectAll("circle").transition()
                    .attr("cx", 860)
                    .attr("cy", function() { indexEmpty = getEmptySlotIndex(d); return 250 + (indexEmpty * 75);})
                    .duration(400)
                    .each('start', function () {
                    });
                d3.select(this).selectAll("text").transition()
                    .attr("x", 860)
                    .attr("y", function() { return 250 + (indexEmpty * 75);})
                    .duration(400);

                chosenCount++;
                addElementToVenSet(d);
            }
        } else {
            d3.select(this).selectAll("circle").transition()
                .attr("cx", 860)
                .attr("cy", startY)
                .duration(400)
                .each('start', function () {
                });
            d3.select(this).selectAll("text").transition()
                .attr("x", 860)
                .attr("y", startY)
                .duration(400);
            startX = 0;
            startY = 0;
        }
    } else {

        d3.select(this).selectAll("circle").transition()
            .attr("cx", d.initX)
            .attr("cy", d.initY)
            .duration(400);
        d3.select(this).selectAll("text").transition()
            .attr("x", d.initX)
            .attr("y", d.initY)
            .duration(400);
        if (chosenCount > 0) {
            chosenCount--;
            setEmptySlotIndex(d);
        }
        foodJson.push(d);
        removeElementFrmVenSet(d);
    }
    printSlots();
    pageX = 0;
    pageY = 0;

}

function indexOfFoodArray(d) {
    for (var i = 0; i < foodJson.length; i++) {
        if (foodJson[i].label == d.label)
            return i;
    }
    return -1;
}

function indexOfVennArray(d) {
    for (var i = 0; i < sets.length; i++) {
        if (sets[i].label == d.label)
            return i;
    }
    return -1;
}

function getCy(d, i) {
    if (i % 2 == 0)
        return (bubbleHeight + oR) / 4;
    else
        return (bubbleHeight + oR) / 2;
}

function getCx(d, i) {
    return oR*(3*(0.8+(i/2))-1);
}

var combine = function(a, min) {
    var fn = function(n, src, got, all) {
        if (n == 0) {
            if (got.length > 0) {
                all[all.length] = got;
            }
            return;
        }
        for (var j = 0; j < src.length; j++) {
            fn(n - 1, src.slice(j + 1), got.concat([src[j]]), all);
        }
        return;
    }
    var all = [];
    for (var i = min; i < a.length; i++) {
        fn(i, a, [], all);
    }
    all.push(a);
    return all;
}

function removeElementFrmVenSet(info) {
    var localSets=[];
    for (var i = 0; i < sets.length; i++) {
        var index = sets[i].sets.indexOf(info.sets[0]);
        if (index < 0)
            localSets.push(sets[i]);
    }
    sets = localSets;
    startDrawingVenn();
}



function addElementToVenSet(d) {
    // First element in the sets.
    sets.push(d);

    var localArray=[];
    for (var i = 0; i < sets.length; i++) {
        if (sets[i].label) {
            localArray.push(sets[i].sets[0]);
        }
    }

    var localCombo = combine(localArray, 2);

    for (var i = 0; i < localCombo.length; i++) {
        if (localCombo[i].length > 1)
            sets.push({sets: localCombo[i], size:1000});
    }

    startDrawingVenn();
}

function getEmptySlotIndex(d) {

    for (var i = 0; i < slots.length; i++) {
        if (slots[i] == -1) {
            slots[i] = d.sets[0];
            return i;
        }

    }
    return -1;
}

function printSlots() {
    console.log(slots.toString());
}

function setEmptySlotIndex(d) {
    for (var i = 0; i < slots.length; i++) {
        if (slots[i] == d.sets[0]) {
            slots[i] = -1;
        }
    }
}

var lastSelectedItemId;
var selectedLocation = "";
function selectLocation(selectedItem) {

    if (lastSelectedItemId && lastSelectedItemId != selectedItem)
        document.getElementById(lastSelectedItemId).style.backgroundColor = "#FFE4C4";
    document.getElementById(selectedItem).style.backgroundColor = "#808080";
    lastSelectedItemId = selectedItem;
    selectedLocation = document.getElementById(selectedItem).id;

}

function parseURLParams(url) {
    var queryStart = url.indexOf("?") + 1,
        queryEnd   = url.indexOf("#") + 1 || url.length + 1,
        query = url.slice(queryStart, queryEnd - 1),
        pairs = query.replace(/\+/g, " ").split("&"),
        parms = {}, i, n, v, nv;

    if (query === url || query === "") {
        return;
    }

    for (i = 0; i < pairs.length; i++) {
        nv = pairs[i].split("=");
        n = decodeURIComponent(nv[0]);
        v = decodeURIComponent(nv[1]);

        if (!parms.hasOwnProperty(n)) {
            parms[n] = [];
        }

        parms[n].push(nv.length === 2 ? v : null);
    }
    return parms.attributes[0];
}

function getRestaurantList(cuisines) {

    if (cuisines == null || cuisines == "") {
        alert("Select cuisines");
        return;
    }

    if (selectedLocation == null || selectedLocation == "") {
        alert("Select a location");
        return;
    }

    if (indexAttributes == null || indexAttributes == "") {
        alert("Go back to home page and select attributes");
        return;
    }
    console.log(cuisines);
    console.log(selectedLocation);
    console.log(indexAttributes);
    var link = "http://yelp-reco-dv.herokuapp.com/recommend?location=" + selectedLocation + "&categories=" + cuisines + "&preferences=" + indexAttributes;
    httpGet(link);
}

function httpGet(url)
{
    var xhr = createCORSRequest('GET', url);
    if (!xhr) {
        alert('CORS not supported');
        return;
    }

    // Response handlers.
    xhr.onload = function() {
        var text = xhr.responseText;
        var jsonResponse = JSON.parse(text);
        console.log(jsonResponse[0]);


        var pos = jsonResponse[0].pos;
        var neg = jsonResponse[0].neg;
        if (pos == "undefined")
            pos = 0;

        if (neg == "undefined")
            neg = 0;
        donutPosNeg(pos, neg);

        var star1 = jsonResponse[0].star1;
        var star2 = jsonResponse[0].star2;
        var star3 = jsonResponse[0].star3;
        var star4 = jsonResponse[0].star4;
        var star5 = jsonResponse[0].star5;

        donutRating(star1, star2, star3, star4, star5);


        var restaurantName = jsonResponse[0].name;
        var restaurantaddress = jsonResponse[0].address;

        document.getElementById("catList").innerHTML = "<p align='cener'><h2>" + restaurantName + "</h2><br> " + restaurantaddress + "</p>";
        console.log(pos + ", " + neg + ", " + star1 + ", " + star2 +", " + star3 + ", " + star4 + ", " + star5);

    };

    xhr.onerror = function(e) {
        console.log(e);
    };
    xhr.send();

}

function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        // CORS not supported.
        xhr = null;
    }
    return xhr;
}
