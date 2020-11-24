<!doctype html>
<html ng-app="app">

<head>
    <base href="/">
    <meta charset="utf-8">
    <meta name="theme-color" content="#080B17">

    <title>Betppro - adm</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="app/css/ui-grid.min.css" rel="stylesheet">
    <link rel="icon" type="image/png" href="app/img/favicon.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="app/css/style.min.css" />
    <link rel="stylesheet" type="text/css" href="app/css/sweetalert.min.css" />
    <link rel="stylesheet" href="app/css/angular-material.min.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous">


</head>

<body>

    <div class="center-loder" ng-show="loader">
        <div class="lds-default">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>

    <div class="center-loder lds-hourglass" ng-show="loader"></div>

    <div data-ng-view="" id="ng-view"></div>

</body>

<script
        src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<script type="text/javascript" src="app/js/lib/angular.min.js?v1"></script>
<script type="text/javascript" src="app/js/lib/ui-grid.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-messages.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-route.min.js"></script>
<script type="text/javascript" src="app/js/lib/ng-map.min.js"></script>
<script type="text/javascript" src="app/js/lib/hamster.min.js"></script>
<script type="text/javascript" src="app/js/lib/mousewheel.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-aria.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-animate.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-material.min.js"></script>
<script type="text/javascript" src="app/js/lib/moment.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-growl.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/limonte-sweetalert2/7.29.2/sweetalert2.all.js"></script>
<script type="text/javascript" src="app/js/lib/sweetalert-dev.min.js"></script>
<script type="text/javascript" src="app/js/lib/SweetAlert.min.js"></script>
<script type="text/javascript" src="app/js/lib/pdfmake.min.js"></script>
<script type="text/javascript" src="app/js/lib/vfs_fonts.min.js"></script>
<script type="text/javascript" src="app/js/lib/lodash.min.js"></script>
<script type="text/javascript" src="app/js/lib/jszip.min.js"></script>
<script type="text/javascript" src="app/js/lib/excel-builder.dist.js"></script>
<script type="text/javascript" src="app/js/lib/angular-io-barcode.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-recaptcha.min.js?v1"></script>
<script type="text/javascript" src="app/js/lib/ng-device-detector.min.js"></script>
<script type="text/javascript" src="app/js/lib/re-tree.min.js"></script>
<script type="text/javascript" src="app/js/lib/i18n/angular-locale_es-co.min.js"></script>
<script type="text/javascript" src="app/js/lib/ui-bootstrap-tpls.min.js?v2"></script>
<script type="text/javascript" src="app/js/lib/cleave-angular.min.js"></script>
<script type="text/javascript" src="app/js/lib/cleave-phone.co.min.js"></script>
<script type="text/javascript" src="app/js/lib/angular-filter.min.js"></script>
<script type="text/javascript" src="app/js/lib/ocLazyLoad.require.min.js"></script>
<script type="text/javascript" src="app/js/lib/ocLazyLoad.min.js"></script>
<script type="text/javascript" src="index.js"></script>
<script type="text/javascript" src="routes.js"></script>
<script type="text/javascript" src="app/js/constants.min.js"></script>
<script type="text/javascript" src="app/js/directives/common.min.js"></script>
<script type="text/javascript" src="app/js/services/general.service.min.js"></script>
<script type="text/javascript" src="app/js/filters/main.filter.min.js"></script>
<script type="text/javascript" src="app/js/filters/angular-filter.js"></script>
<script type="text/javascript" src="app/js/controllers/header.ctrl.min.js"></script>
<script type="text/javascript" src="app/js/controllers/footer.ctrl.min.js"></script>
<script type="text/javascript" src="app/js/controllers/buscadorRed.ctrl.js"></script>
<script src="http://cdn.zingchart.com/zingchart.min.js"></script>
<script src="app/js/directives/chart.js"></script>

</html>