<!--
    Страница "О ферме"
    Использует стили из stile.txt
    Адаптирована под общий дизайн проекта
-->
<link rel="stylesheet" type="text/css" href="/static/content/site.css"/>

<div class="container">
    <!-- О ферме -->
    <div class="about-card">
        <h2 class="about-card__title">О ферме</h2>
        <div class="about-card__content">
            <div class="about-flex-container">
                <div class="about-text-content">
                    <h3>Чем мы занимаемся?</h3>
                    <ul class="about-list">
                        <li>Выращивание ягод</li>
                        <li>Прямые продажи</li>
                        <li>Оптовые поставки</li>
                        <li>Переработка ягод</li>
                    </ul>
                    <p>Наша ферма — это не просто бизнес. Это место, где каждая ягода выращена с душой и заботой. Мы бережно относимся к традициям натурального земледелия, используя современные агротехнологии и всегда ставим качество во главу угла.</p>
                    <p>Мы гордимся тем, что можем предложить вам продукцию, которая сохраняет вкус и пользу лета. Прямые поставки с фермы гарантируют свежесть, а прозрачность производства — ваше спокойствие.</p>
                </div>
                <div class="about-image-right">
                    <img src="/static/images/клубника_грядка.jpg" alt="Сбор клубники на ферме" class="rounded-square-img">
                </div>
            </div>
        </div>
    </div>

    <!-- Прямые продажи -->
    <div class="about-card feature-card">
        <div class="feature-content">
            <div class="feature-text">
                <h2 class="feature-title">🍓 Прямые продажи</h2>
                <p>Покупайте свежие ягоды напрямую с фермы по самым выгодным ценам! Мы предлагаем:</p>
                <ul class="feature-list">
                    <li>Свежий сбор в день заказа</li>
                    <li>Индивидуальный подход</li>
                    <li>Скидки постоянным клиентам</li>
                    <li>Доставка по городу и области</li>
                </ul>
                <a href="/contacts" class="feature-btn">Заказать сейчас →</a>
            </div>
            <div class="feature-image">
                <img src="/static/images/лавка_ягод.jpg" alt="Прямые продажи ягод" class="feature-img">
            </div>
        </div>
    </div>

    <!-- Оптовые продажи -->
    <div class="about-card feature-card reverse">
        <div class="feature-content">
            <div class="feature-image">
                <img src="/static/images/объём_ягод.jpg" alt="Оптовые продажи" class="feature-img">
            </div>
            <div class="feature-text">
                <h2 class="feature-title">📦 Оптовые продажи</h2>
                <p>Для ресторанов, кафе, магазинов и производителей. Работаем с юридическими лицами:</p>
                <ul class="feature-list">
                    <li>Гибкая система скидок</li>
                    <li>Регулярные поставки</li>
                    <li>Сертификаты качества</li>
                    <li>Индивидуальные условия сотрудничества</li>
                </ul>
                <a href="/contacts" class="feature-btn">Стать партнером →</a>
            </div>
        </div>
    </div>

    <!-- Декоративный разделитель -->
    <div class="divider">
        <img src="/static/images/разделитель_бант.jpg" alt="Разделитель">
    </div>

    <!-- Наши ягоды -->
    <div class="about-card">
        <h2 class="about-card__title">Наши ягоды</h2>
        <div class="about-card__content">
            <div class="berries-showcase">
                <div class="berry-card">
                    <div class="berry-image">
                        <img src="/static/images/клубника_наши_ягоды.jpg" alt="Клубника" class="berry-img">
                    </div>
                    <h3 class="berry-name">Клубника</h3>
                    <p class="berry-desc">Сладкая, сочная, ароматная</p>
                </div>
                
                <div class="berry-card">
                    <div class="berry-image">
                        <img src="/static/images/малина_наши_ягоды.jpg" alt="Малина" class="berry-img">
                    </div>
                    <h3 class="berry-name">Малина</h3>
                    <p class="berry-desc">Нежная, полезная, витаминная</p>
                </div>
                
                <div class="berry-card">
                    <div class="berry-image">
                        <img src="/static/images/голубика_наши_ягоды.jpg" alt="Голубика" class="berry-img">
                    </div>
                    <h3 class="berry-name">Голубика</h3>
                    <p class="berry-desc">Целебная, богатая антиоксидантами</p>
                </div>
            </div>
            
            <div class="about-berries__note">
                <p><strong>Примечание:</strong> Мы заботимся о качестве на всех этапах производства! Каждая ягода проходит строгий отбор, чтобы вы получили только лучший продукт.</p>
            </div>
        </div>
    </div>

    <!-- Декоративный разделитель -->
    <div class="divider">
        <img src="/static/images/разделитель_бант.jpg" alt="Разделитель">
    </div>

    <!-- Сорта и производство -->
    <div class="about-card">
        <h2 class="about-card__title">Сорта и производство</h2>
        <div class="about-card__content">
            <div class="about-two-columns">
                <div class="about-column">
                    <h3>Какие сорта выращиваем?</h3>
                    <ul class="about-list">
                        <li>Клубника: Эльсанта, Хоней, Клери</li>
                        <li>Малина: Геракл, Гусар, Жёлтый гигант</li>
                        <li>Голубика: Блюкроп, Патриот, Спартан</li>
                    </ul>
                </div>
                <div class="about-column">
                    <h3>Производство</h3>
                    <ul class="about-list">
                        <li>Собственные теплицы и открытый грунт</li>
                        <li>Капельный полив и органические удобрения</li>
                        <li>Ручной сбор ягод</li>
                        <li>Современные цеха заморозки и хранения</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- Декоративный разделитель -->
    <div class="divider">
        <img src="/static/images/разделитель_бант.jpg" alt="Разделитель">
    </div>

    <!-- Переработка (с изображением) -->
    <div class="about-card feature-card">
        <div class="feature-content">
            <div class="feature-text">
                <h2 class="feature-title">🏭 Переработка</h2>
                <p>Мы не только выращиваем ягоды, но и предлагаем продукцию собственной переработки:</p>
                <ul class="feature-list">
                    <li>🍯 Джемы и варенье</li>
                    <li>❄️ Замороженные ягоды</li>
                    <li>🧃 Натуральные соки</li>
                    <li>🍬 Пастила без сахара</li>
                </ul>
                <p class="processing-note">Все продукты изготавливаются без консервантов и искусственных добавок, сохраняя максимум пользы и натуральный вкус.</p>
                <a href="/contacts" class="feature-btn">Узнать подробнее →</a>
            </div>
            <div class="feature-image">
                <img src="/static/images/джем.jpg" alt="Переработка ягод" class="feature-img">
            </div>
        </div>
    </div>
</div>