<div class="container partners-container">
    <h1>Партнёрские компании</h1>
    
    <!-- Глобальная ошибка -->
    % if error:
    <div class="row">
        <div class="col-md-12">
            <div class="alert alert-danger">
                <strong>Ошибка:</strong> {{ error }}
                <button type="button" class="close" data-dismiss="alert">x</button>
            </div>
        </div>
    </div>
    % end
    
    <!-- Форма добавления -->
    <div class="partner-form-card">
        <h2>Предложить сотрудничество</h2>
        <form action="/add_partner" method="post">
            <div class="form-row">
                <div class="form-group">
                    <label>Наименование компании *</label>
                    <input type="text" name="author" value="{{ author or '' }}">
                    % if field_errors.get('author'):
                    <div class="field-error">{{ field_errors['author'] }}</div>
                    % end
                </div>
                <div class="form-group">
                    <label>Телефон * (+71234567890)</label>
                    <input type="text" name="phone" value="{{ phone or '' }}" placeholder="+79123456789">
                    % if field_errors.get('phone'):
                    <div class="field-error">{{ field_errors['phone'] }}</div>
                    % end
                </div>
                <div class="form-group">
                    <label>Дата *</label>
                    <input type="date" name="date" value="{{ date or '' }}">
                    % if field_errors.get('date'):
                    <div class="field-error">{{ field_errors['date'] }}</div>
                    % end
                </div>
            </div>
            <div class="form-group">
                <label>Описание сотрудничества *</label>
                <textarea name="description" rows="3">{{ description or '' }}</textarea>
                % if field_errors.get('description'):
                <div class="field-error">{{ field_errors['description'] }}</div>
                % end
            </div>
            <button type="submit" class="btn-primary">Разместить →</button>
        </form>
    </div>

    <!-- Список партнёров -->
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