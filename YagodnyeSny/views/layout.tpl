<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'Ягодные сны' }} - Ягодная ферма</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css"/>
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .container.body-content {
            flex: 1;
            width: 100%;
            max-width: 100%;
            padding: 0;
            margin: 0;
        }
    </style>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <a href="/" class="navbar-brand">
                    Ягодные сны
                </a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li {{ 'class="active"' if active_page == 'about' else '' }}>
                        <a href="/about">О ферме</a></li>
                    <li {{ 'class="active"' if active_page == 'jobs' else '' }}>
                        <a href="/jobs">Вакансии</a></li>
                    <li {{ 'class="active"' if active_page == 'contacts' else '' }}>
                        <a href="/contacts">Контакты</a></li>
                    <li {{ 'class="active"' if active_page == 'partners' else '' }}>
                        <a href="/partners">Партнёры</a></li>
                </ul>
            </div>
        </div>
    </div>

    {{!base}}

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
</body>
</html>