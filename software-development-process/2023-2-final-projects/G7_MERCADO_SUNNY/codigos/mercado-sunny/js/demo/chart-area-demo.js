
// Grafico das categorias mais vendidas
var options = {
    chart: {
      height: 400,
      type: 'bar'
    },
    colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#2b908f', '#f9a3a4', '#90ee7e',
        '#f48024', '#69d2e7'
    ],
    series: [{
      name: 'quantidade',
      data: [250,150,100,50,65,60,70,91,125]
    }],
    xaxis: {
      categories: ["Alimentos básicos",'Hortifrutí',"Padaria","Bebidas","Congelados","Produtos de Limpeza","Higiene Pessoal", "Petshop","Farmácia"]
    }
}
  
  var chart = new ApexCharts(document.querySelector("#chartCategoria"), options);
  
  chart.render();





//Gráfico renda por mes
  var options = {
    series: [{
    name: 'Inflation',
    data:[8000, 9000, 8500, 10000, 9500, 11500, 11000, 10500, 9500, 10000, 9200, 8800]
  }],
    chart: {
    height: 500,
    type: 'bar',
  },
  plotOptions: {
    bar: {
      borderRadius: 1,
      dataLabels: {
        position: 'top', // top, center, bottom
      },
    }
  },
  dataLabels: {
    enabled: true,
    formatter: function (val) {
      return val;
    },
    offsetY: -20,
    style: {
      fontSize: '12px',
      colors: ["#304758"]
    }
  },
  
  xaxis: {
    categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    position: 'top',
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    },
    crosshairs: {
      fill: {
        type: 'gradient',
        gradient: {
          colorFrom: '#D8E3F0',
          colorTo: '#BED1E6',
          stops: [0, 100],
          opacityFrom: 0.4,
          opacityTo: 0.5,
        }
      }
    },
    tooltip: {
      enabled: true,
    }
  },
  yaxis: {
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false,
    },
    labels: {
      show: false,
      formatter: function (val) {
        return val;
      }
    }
  
  },
  
  };

  var chart = new ApexCharts(document.querySelector("#chartMes"), options);
  chart.render();