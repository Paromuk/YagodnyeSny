<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'Ягодные сны' }} - Ягодная ферма</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">
                    <span style="font-size: 1.2rem;">🍓</span> Ягодные сны
                </a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li {{ 'class=active' if active_page == 'home' else '' }}>
                        <a href="/">Главная</a></li>
                    <li {{ 'class=active' if active_page == 'about' else '' }}>
                        <a href="/about">О ферме</a></li>
                    <li {{ 'class=active' if active_page == 'jobs' else '' }}>
                        <a href="/jobs">Вакансии</a></li>
                    <li {{ 'class=active' if active_page == 'contacts' else '' }}>
                        <a href="/contacts">Контакты</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        <h1>{{ title or 'Ягодные сны' }}</h1>
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - Ягодная ферма "Ягодные сны"</p>
            <p class="text-muted">Учебный проект.</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>

