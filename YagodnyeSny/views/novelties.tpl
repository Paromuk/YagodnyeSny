<link rel="stylesheet" type="text/css" href="/static/content/novelties.css"/>

<div class="container novelties-container">
    <div class="novelties-header">
        <h1>Актуальные новинки</h1>
        <p>Самые свежие новости и новинки с нашей фермы</p>
    </div>

    <!-- Сообщение об успехе -->
    % if success_message:
        <div class="success-message">
            {{success_message}}
        </div>
    % end

    <!-- Форма для добавления новинки -->
    <div class="novelty-form-card">
        <h2>Добавить новинку</h2>
        <form method="post" action="/novelties" id="noveltyForm">
            <div class="form-group">
                <label for="author">Автор (Имя/Ник) *</label>
                <input type="text" 
                       class="form-control" 
                       id="author" 
                       name="author" 
                       value="{{form_data.get('author', '')}}"
                       placeholder="Example: John or John.Doe"
                       pattern="[A-Za-zА-Яа-яЁё0-9\s\.]{2,50}"
                       title="Only letters, digits (max 4), spaces and dot (.)"
                       required>
                <small class="form-text text-muted">Только буквы, цифры (не более 4), пробелы, дефисы и точки. От 2 до 50 символов</small>
                % if errors.get('author'):
                    <div class="invalid-feedback">{{errors['author']}}</div>
                % end
            </div>

            <div class="form-group">
                <label for="title">Наименование новинки *</label>
                <input type="text" 
                       class="form-control" 
                       id="title" 
                       name="title" 
                       value="{{form_data.get('title', '')}}"
                       placeholder="Example: New sweet strawberry!"
                       pattern="[A-Za-zА-Яа-яЁё0-9\s\.\,\!\\?]{3,100}"
                       title="Only letters, digits, spaces and punctuation (. , ! ?)"
                       required>
                <small class="form-text text-muted">От 3 до 100 символов, не может состоять только из цифр</small>
                % if errors.get('title'):
                    <div class="invalid-feedback">{{errors['title']}}</div>
                % end
            </div>

            <div class="form-group">
                <label for="description">Описание *</label>
                <textarea class="form-control" 
                          id="description" 
                          name="description" 
                          rows="3"
                          placeholder="Example: We have developed a new variety! It is very sweet and tasty."
                          pattern="[A-Za-zА-Яа-яЁё0-9\s\.\,\!\\?\n]{10,500}"
                          title="Only letters, digits, spaces, punctuation (. , ! ?) and line breaks"
                          required>{{form_data.get('description', '')}}</textarea>
                <small class="form-text text-muted">От 10 до 500 символов, не может состоять только из цифр</small>
                % if errors.get('description'):
                    <div class="invalid-feedback">{{errors['description']}}</div>
                % end
            </div>

            <div class="form-group">
                <label for="date">Дата *</label>
                <input type="date" 
                       class="form-control {{'is-invalid' if errors.get('date') else ''}}" 
                       id="date" 
                       name="date" 
                       value="{{form_data.get('date', '')}}"
                       min="{{min_date}}"
                       max="{{max_date}}"
                       required>
                <small class="form-text text-muted">Дата не может быть раньше {{today_date}} и позже {{max_date_display}}</small>
                % if errors.get('date'):
                    <div class="invalid-feedback">{{errors['date']}}</div>
                % end
            </div>

            % if errors.get('general'):
                <div class="alert alert-danger">{{errors['general']}}</div>
            % end

            <button type="submit" class="btn-submit">Разместить новинку</button>
        </form>
    </div>

    <!-- Список новинок -->
    <div class="novelties-list">
        <h2>Список новинок</h2>
        % if not novelties:
            <div class="empty-state">
                <p>Пока нет добавленных новинок. Будьте первым!</p>
            </div>
        % else:
            <div class="novelties-grid">
                % for item in novelties:
                    <div class="novelty-card">
                        <div class="novelty-header">
                            <h3 class="novelty-title">{{item.get('title', 'Без названия')}}</h3>
                            <span class="novelty-date">{{item.get('date_formatted', item.get('date_added', 'Дата не указана'))}}</span>
                        </div>
                        <div class="novelty-body">
                            <p class="novelty-description">{{item.get('description', '')}}</p>
                        </div>
                        <div class="novelty-footer">
                            <span class="novelty-author">Автор: {{item.get('author', 'Аноним')}}</span>
                            <span class="novelty-id">ID: {{item.get('id', '')}}</span>
                        </div>
                    </div>
                % end
            </div>
        % end
    </div>
</div>
