
  
  // ---------- CHARTS ----------
  
  // // BAR CHART
  // var barChartOptions = {
  //   series: [{
  //     data: [10, 8, 6, 4, 2],
  //     name: "Memberships sales",
  //   }],
  //   chart: {
  //     type: "bar",
  //     background: "transparent",
  //     height: 350,
  //     toolbar: {
  //       show: false,
  //     },
  //   },
  //   colors: [
  //     "#2962ff",
  //     "#d50000",
  //     "#2e7d32",
  //     "#ff6d00",
  //     "#583cb3",
  //   ],
  //   plotOptions: {
  //     bar: {
  //       distributed: true,
  //       borderRadius: 4,
  //       horizontal: false,
  //       columnWidth: "40%",
  //     }
  //   },
  //   dataLabels: {
  //     enabled: false,
  //   },
  //   fill: {
  //     opacity: 1,
  //   },
  //   grid: {
  //     borderColor: "#55596e",
  //     yaxis: {
  //       lines: {
  //         show: true,
  //       },
  //     },
  //     xaxis: {
  //       lines: {
  //         show: true,
  //       },
  //     },
  //   },
  //   legend: {
  //     labels: {
  //       colors: "#f5f7ff",
  //     },
  //     show: true,
  //     position: "top",
  //   },
  //   stroke: {
  //     colors: ["transparent"],
  //     show: true,
  //     width: 2
  //   },
  //   tooltip: {
  //     shared: true,
  //     intersect: false,
  //     theme: "dark",
  //   },
  //   xaxis: {
  //     categories: ["Laptop", "Phone", "Monitor", "Headphones", "Camera"],
  //     title: {
  //       style: {
  //         color: "#f5f7ff",
  //       },
  //     },
  //     axisBorder: {
  //       show: true,
  //       color: "#55596e",
  //     },
  //     axisTicks: {
  //       show: true,
  //       color: "#55596e",
  //     },
  //     labels: {
  //       style: {
  //         colors: "#f5f7ff",
  //       },
  //     },
  //   },
  //   yaxis: {
  //     title: {
  //       text: "Count",
  //       style: {
  //         color:  "#f5f7ff",
  //       },
  //     },
  //     axisBorder: {
  //       color: "#55596e",
  //       show: true,
  //     },
  //     axisTicks: {
  //       color: "#55596e",
  //       show: true,
  //     },
  //     labels: {
  //       style: {
  //         colors: "#f5f7ff",
  //       },
  //     },
  //   }
  // };
  
  // var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
  // barChart.render();
  
  
  // // AREA CHART
  // var areaChartOptions = {
  //   series: [{
  //     name: "Membership sales",
  //     data: [31, 40, 28, 51, 42, 109, 100],
  //   }, {
  //     name: "Machinery Purchase",
  //     data: [11, 32, 45, 32, 34, 52, 41],
  //   }],
  //   chart: {
  //     type: "area",
  //     background: "transparent",
  //     height: 350,
  //     stacked: false,
  //     toolbar: {
  //       show: false,
  //     },
  //   },
  //   colors: ["#00ab57", "#d50000"],
  //   labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
  //   dataLabels: {
  //     enabled: false,
  //   },
  //   fill: {
  //     gradient: {
  //       opacityFrom: 0.4,
  //       opacityTo: 0.1,
  //       shadeIntensity: 1,
  //       stops: [0, 100],
  //       type: "vertical",
  //     },
  //     type: "gradient",
  //   },
  //   grid: {
  //     borderColor: "#55596e",
  //     yaxis: {
  //       lines: {
  //         show: true,
  //       },
  //     },
  //     xaxis: {
  //       lines: {
  //         show: true,
  //       },
  //     },
  //   },
  //   legend: {
  //     labels: {
  //       colors: "#f5f7ff",
  //     },
  //     show: true,
  //     position: "top",
  //   },
  //   markers: {
  //     size: 6,
  //     strokeColors: "#1b2635",
  //     strokeWidth: 3,
  //   },
  //   stroke: {
  //     curve: "smooth",
  //   },
  //   xaxis: {
  //     axisBorder: {
  //       color: "#55596e",
  //       show: true,
  //     },
  //     axisTicks: {
  //       color: "#55596e",
  //       show: true,
  //     },
  //     labels: {
  //       offsetY: 5,
  //       style: {
  //         colors: "#f5f7ff",
  //       },
  //     },
  //   },
  //   yaxis: 
  //   [
  //     {
  //       title: {
  //         text: "Purchase Orders",
  //         style: {
  //           color: "#f5f7ff",
  //         },
  //       },
  //       labels: {
  //         style: {
  //           colors: ["#f5f7ff"],
  //         },
  //       },
  //     },
  //     {
  //       opposite: true,
  //       title: {
  //         text: "Sales Orders",
  //         style: {
  //           color:  "#f5f7ff",
  //         },
  //       },
  //       labels: {
  //         style: {
  //           colors: ["#f5f7ff"],
  //         },
  //       },
  //     },
  //   ],
  //   tooltip: {
  //     shared: true,
  //     intersect: false,
  //     theme: "dark",
  //   }
  // };
  
  // var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
  // areaChart.render();
  var options = {
    series: [{
    name: 'Inflation',
    data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
  }],
    chart: {
    height: 350,
    type: 'bar',
  },
  plotOptions: {
    bar: {
      borderRadius: 10,
      dataLabels: {
        position: 'top', // top, center, bottom
      },
    }
  },
  dataLabels: {
    enabled: true,
    formatter: function (val) {
      return val + "%";
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
        return val + "%";
      }
    }
  
  },
  title: {
    text: 'Monthly Membership Sales',
    floating: true,
    offsetY: 330,
    align: 'center',
    style: {
      color: '#444'
    }
  }
  };

  var chart = new ApexCharts(document.querySelector("#area-chart"), options);
  chart.render();