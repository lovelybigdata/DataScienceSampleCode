<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>A Django Girl's Adventure</title>
    <link href="//fonts.googleapis.com/css?family=Lemon" rel="stylesheet" type="text/css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="//djangogirlstaipei.github.io/assets/css/style.css" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="header">
        <h1 class="site-title text-center">
            <a href="/">A Django Girl's Adventure</a>
        </h1>
    </div>
    <div class="container post post-detail">
        <div class="post-heading">
            <h1 class="title"><a href="">{{ post['title'] }}</a>
            </h1>
        </div>
        <div class="location">
            <i class="fa fa-map-marker"></i>
            <span id="location-content">{{ post['location'] }}</span>
        </div>
        <div id="map-canvas" class="map"></div>
        <div class="post-content">
            {{ post['content'] }}
        </div>
        <hr class="fancy-line">
        <img class="photo" src="{{ post['photo'] }}" alt="">
    </div>
    <script src="//maps.googleapis.com/maps/api/js?v=3.exp&libraries=places&sensor=false"></script>
    <script src="//djangogirlstaipei.github.io/assets/js/map.js"></script>
</body>
</html>