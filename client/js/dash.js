require([], function() {
  var color_map = {
    0 : "#eee",
    1 : "#eee",
    2 : "#85d6e6",
    3 : "#658cc6",
    4 : "#4044a3",
    5 : "#231e68"
  };

  var width = 960,
  height = 136,
  cellSize = 15; // cell size

  var draw_graph_outlines = function(){

    var day = d3.time.format("%w"),
    week = d3.time.format("%U"),
    percent = d3.format(".1%"),
    format = d3.time.format("%Y-%m-%d");

    var svg = d3.select("body").selectAll("svg")
      .data(['', '', ''])
      .enter().append("svg")
      .attr("width", width)
      .attr("height", height)
      .attr("class", "RdYlGn")
      .append("g")
      .attr("transform", "translate(" + ((width - cellSize * 53) / 2) + "," + (height - cellSize * 7 - 1) + ")");

    var YEAR = 31449600000;
    var DAY = 86400000;
    var today = new Date();
    var year_ago = new Date(today.getTime() - YEAR);
    var start = year_ago;
    var end = today;

    var s_year = start.getFullYear();
    var e_year = end.getFullYear();
    var DAY = 24*60*60*1000;
    var num_years = (e_year - s_year) + 1;
    var padding = start.getDay() + 1;

    var multi_week = function (d){
      var date = new Date(d);
      var diffDays = Math.round(Math.abs((start.getTime() - date.getTime())/DAY));
      diffDays += padding;
      var week = Math.floor((diffDays)/7);
      return week;
    };

    var rect = svg.selectAll(".day")
      .data(function(d) { return d3.time.days(start, end); })
      .enter().append("rect")
      .attr("class", "day")
      .attr("width", cellSize)
      .attr("height", cellSize)
      .attr("x", function(d) { return multi_week(d) * cellSize; })
      .attr("y", function(d) { return day(d) * cellSize; })
      .datum(format);

    rect.append("title")
      .text(function(d) { return d; });

    return svg;
  };
  // Loads data
  /** /

      d3.csv("dji.csv", function(error, csv) {
      var data = d3.nest()
      .key(function(d) { return d.Date; })
      .rollup(function(d) { return (d[0].Close - d[0].Open) / d[0].Open; })
      .map(csv);

      rect.filter(function(d) { return d in data; })
      .attr("class", function(d) { return "day " + color(data[d]); })
      .select("title")
      .text(function(d) { return d + ": " + percent(data[d]); });
      });

  d3.json(user + 'exercise', function(error, json) {
    var max;
    _.each(json, function(value, key) {
      if (max == null || value > max) { max = value; }
    });
    var color = function(d){
      if (d === 0){
        return 0;
      } else {
        return Math.floor((d/max) * 4) + 1;
      }
    };

    rect.filter(function(d) {console.log(json);return d in json; })
      .attr("class", function(d) { return "day q" + color(json[d]); })
      .select("title")
      .text(function(d) { return d + ": " + json[d] + " contributions "; });
    // Accomodate singular.
  });

  d3.select(self.frameElement).style("height", "2910px");
      /**/
  // Replace all SVG images with inline SVG
  $('img.svg').each(function(){
    var $img = $(this);
    var imgID = $img.attr('id');
    var imgClass = $img.attr('class');
    var imgURL = $img.attr('src');
    var imgTitle = $img.attr('title');

    $.get(imgURL, function(data) {
      // Get the SVG tag, ignore the rest
      var $svg = $(data).find('svg');

      // Add replaced image's ID to the new SVG
      if(typeof imgID !== 'undefined') {
        $svg = $svg.attr('id', imgID);
      }
      // Add replaced image's classes to the new SVG
      if(typeof imgClass !== 'undefined') {
        $svg = $svg.attr('class', imgClass+' replaced-svg');
      }

      if(typeof imgTitle !== 'undefined') {
        $svg = $svg.attr('title', imgTitle);
      }

      // Remove any invalid XML tags as per http://validator.w3.org
      $svg = $svg.removeAttr('xmlns:a');

      // Replace image with new SVG
      $img.replaceWith($svg);

    }, 'xml');

  });

  var draw_labels = function(graph, labels){
    graph.data(labels)
      .enter();

    graph.attr("id", function(d) { return d; });

    graph.append("text")
      .attr("transform", "translate(-6," + cellSize * 3.5 + ")rotate(-90)")
      .style("text-anchor", "middle")
      .text(function(d) { return d; });

  };

  var populate_graphs = function(user, graph, names){
    for (n in names){
      d3.json(user + '/'+ names[n], function(error, json) {
        var max;
        _.each(json.data, function(value, key) {
          if (max == null || value > max) { max = value; }
        });
        console.log(max);
        var color = function(d){
          if (d === 0){
            return 0;
          } else if (d === max){
            return 4;
          } else {
            return Math.floor((d/max) * 4) + 1;
          }
        };
        var data = json.data;
        console.log(json.name);
        console.log(data);
        d3.select('#' + json.name).selectAll('.day').filter(function(d) { return d in data; })
        .attr("class", function(d) { return "day q" + color(json.data[d]); })
        .select("title")
        .text(function(d) { return d + ": " + data[d] + " contributions "; });
      // Accomodate singular.
      });
    }

    /** /
      graph.selectAll(".year").filter(function(d) {console.log(json);return d in json; })
        .attr("class", function(d) { return "day q" + color(json[d]); })
        .select("title")
        .text(function(d) { return d + ": " + json[d] + " contributions "; });
      // Accomodate singular.
    });
    /**/
    d3.select(self.frameElement).style("height", "2910px");
  };

////////////////////////
  var user = $("#user").attr("user");
  var g = draw_graph_outlines();

  $.getJSON(user + '/data', function(data){
    draw_labels(g, data.graphs);
    populate_graphs(data.name, g, data.graphs);
  });

});
