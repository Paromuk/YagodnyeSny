<div class="container partners-container">
    <h1>Партнёрские компании</h1>
    
    <!-- Форма добавления -->
    <div class="partner-form-card">
        <h2>📝Предложить сотрудничество</h2>
        <form action="/add_partner" method="post">
            <div class="form-row">
                <div class="form-group">
                    <label>Наименование компании *</label>
                    <input type="text" name="author" value="{{ author or '' }}" required>
                </div>
                <div class="form-group">
                    <label>Телефон *</label>
                    <input type="text" name="phone" value="{{ phone or '' }}" placeholder="+79123456789" required>
                </div>
                <div class="form-group">
                    <label>Дата *</label>
                    <input type="date" name="date" value="{{ date or '' }}" required>
                </div>
            </div>
            <div class="form-group">
                <label>Описание сотрудничества *</label>
                <textarea name="description" rows="3" required>{{ description or '' }}</textarea>
            </div>
            <button type="submit" class="btn-primary">Разместить →</button>
        </form>
        % if error:
            <div class="error-message">{{ error }}</div>
        % end
    </div>

    <!-- Список партнёров (горизонтальные карточки) -->
    <div class="partners-list">
        <h2>Наши партнёры</h2>
        <div class="partners-grid">
            % for partner in partners_list:
            <div class="partner-card">
                <h3>{{ partner['author'] }}</h3>
                <p>{{ partner['description'] }}</p>
                <div class="partner-meta">
                    <span>📞 {{ partner['phone'] }}</span>
                    <span>📅 {{ partner['date'] }}</span>
                </div>
            </div>
            % end
        </div>
    </div>
</div>