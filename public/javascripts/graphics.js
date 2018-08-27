console.log("Estoy akii en grafica")



// Catch buttons
const btnNum1 = document.getElementById("btnNum1");
const btnNum2= document.getElementById("btnNum2");
const btnNum3 = document.getElementById("btnNum3");
const btnNum4 = document.getElementById("btnNum4");


// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages':['corechart','table']});

btnNum1.addEventListener('click',()=>{
 console.log("boton 1")
 // Set a callback to run when the Google Visualization API is loaded.
 google.charts.setOnLoadCallback(draw1());
});

btnNum2.addEventListener('click',()=>{
 console.log("boton 2")
 // Set a callback to run when the Google Visualization API is loaded.
 google.charts.setOnLoadCallback(draw2());
});

btnNum3.addEventListener('click',()=>{
 console.log("boton 3")
 // Set a callback to run when the Google Visualization API is loaded.
 google.charts.setOnLoadCallback(draw3());
});

btnNum4.addEventListener('click',()=>{
 console.log("boton 4")
 // Set a callback to run when the Google Visualization API is loaded.
 google.charts.setOnLoadCallback(draw4());
});

function draw1() {
 // Create the data table.
 
 var data = new google.visualization.DataTable();
 data.addColumn('string', 'Topping');
 data.addColumn('number', 'Slices');
 data.addRows([
  ['Mushrooms', 3],
  ['Onions', 1],
  ['Olives', 1], 
  ['Zucchini', 1],
  ['Pepperoni', 2]
  ]);
 // Set chart options
 var options = {'title':'How Much Pizza I Ate Last Night'
  };
  // Instantiate and draw our chart, passing in some options.
 var chart = new google.visualization.PieChart(document.getElementById('graphics'));
 chart.draw(data, options);
}

function draw2() {

 // Create the data table.
   var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('number', 'Salary');
        data.addColumn('boolean', 'Full Time Employee');
        data.addRows([
          ['Mike',  {v: 10000, f: '$10,000'}, true],
          ['Jim',   {v:8000,   f: '$8,000'},  false],
          ['Alice', {v: 12500, f: '$12,500'}, true],
          ['Bob',   {v: 7000,  f: '$7,000'},  true]
        ]);
        var table = new google.visualization.Table(document.getElementById('graphics'));
         console.log("Lamo a 2");
        table.draw(data, {showRowNumber: true, width: '50%'});
}

function draw3() {
 // Create the data table.jsapii
   var data = google.visualization.arrayToDataTable([
        ["Element", "Density", { role: "style" } ],
        ["Copper", 8.94, "#b87333"],
        ["Silver", 10.49, "silver"],
        ["Gold", 19.30, "gold"],
        ["Platinum", 21.45, "color: #e5e4e2"]
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        title: "Density of Precious Metals, in g/cm^3",
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
        width: '100%', height: '100%'};
      var chart = new google.visualization.ColumnChart(document.getElementById('graphics'));
      chart.draw(view, options);
}

function draw4() {
 // Create the data table.
 var data = new google.visualization.DataTable();
 data.addColumn('string', 'Topping');
 data.addColumn('number', 'Slices');
 data.addRows([
  ['Mushrooms', 3],
  ['Onions', 1],
  ['Olives', 1], 
  ['Zucchini', 1],
  ['Pepperoni', 2]
  ]);
 // Set chart options
 var options = {'title':'How Much Pizza I Ate Last Night', width: '100%', height: '100%'};
  // Instantiate and draw our chart, passing in some options.
 var chart = new google.visualization.BarChart(document.getElementById('graphics'));
 chart.draw(data, options);

}


