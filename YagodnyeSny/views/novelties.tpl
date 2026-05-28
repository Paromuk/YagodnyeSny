<link rel="stylesheet" type="text/css" href="/static/content/novelties.css"/>

<div class="container novelties-container">
    <div class="novelties-header">
        <h1>Актуальные новинки</h1>
        <p>Самые свежие новости и новинки с нашей фермы</p>
    </div>

    % if success_message:
        <div class="success-message">
            {{success_message}}
        </div>
    % end

    <!-- двухколончатая компоновка-->
    <div style="display: flex; gap: 40px; align-items: flex-start;">
        
        <!-- Ллевая колонка - форма -->
        <div style="flex: 0 0 400px;">
            <div class="novelty-form-card" style="background: #f8f9fa; border-radius: 15px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <h2 style="color: #2d6a4f; margin-bottom: 20px; font-size: 24px; margin-top: 0;">Добавить новинку</h2>
                <form method="post" action="/novelties" accept-charset="UTF-8">
                   <div class="form-group">
                        <label for="author">Автор (Имя/Ник) *</label>
                        <input type="text" 
                               class="form-control {{'is-invalid' if errors.get('author') else ''}}" 
                               id="author" 
                               name="author" 
                               value="{{form_data.get('author', '')}}"
                               placeholder="Пример: Иван Петров"
                               pattern="[A-Za-zА-Яа-яЁё0-9\s\.]{2,50}"
                               title="Только буквы, цифры (не более 4), пробелы и максимум одна точка (.)"
                               required>
                        <small class="form-text text-muted">Только буквы, цифры (не более 4), пробелы и максимум одна точка (.) От 2 до 50 символов</small>
                        % if errors.get('author'):
                            <div class="invalid-feedback">{{errors['author']}}</div>
                        % end
                    </div>

                    <div class="form-group">
                        <label for="title">Наименование новинки *</label>
                        <input type="text" 
                               class="form-control {{'is-invalid' if errors.get('title') else ''}}" 
                               id="title" 
                               name="title" 
                               value="{{form_data.get('title', '')}}"
                               placeholder="Пример: Новая сладкая клубника"
                               required>
                        <small class="form-text text-muted">От 3 до 100 символов, не может состоять только из цифр</small>
                        % if errors.get('title'):
                            <div class="invalid-feedback">{{errors['title']}}</div>
                        % end
                    </div>

                    <div class="form-group">
                        <label for="description">Описание *</label>
                        <textarea class="form-control {{'is-invalid' if errors.get('description') else ''}}" 
                                  id="description" 
                                  name="description" 
                                  rows="4"
                                  placeholder="Пример: Мы вывели новый сорт клубники. Он очень сладкий и вкусный!"
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

                    <button type="submit" class="btn-submit" style="width: 100%; background: #2d6a4f; color: white; padding: 10px 25px; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer;">Разместить новинку</button>
                </form>
            </div>
        </div>

        <!-- правая колонка - список новинок -->
        <div style="flex: 1;">
            <div class="novelties-list" style="background: #f8f9fa; border-radius: 15px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: flex; flex-direction: column; max-height: 600px;">
                <h2 style="color: #2d6a4f; margin-bottom: 20px; font-size: 24px; margin-top: 0; flex-shrink: 0;">Список новинок</h2>
                
                <!-- контейнер с прокруткой -->
                <div style="flex: 1; overflow-y: auto; padding-right: 10px;">
                    % if not novelties:
                        <div class="empty-state" style="text-align: center; padding: 40px; background: white; border-radius: 12px; color: #666;">
                            <p>Пока нет добавленных новинок. Будьте первым!</p>
                        </div>
                    % else:
                        <div style="display: flex; flex-direction: column; gap: 15px;">
                            % for item in novelties:
                                <div class="novelty-card" style="background: white; border-radius: 12px; padding: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #2d6a4f; transition: transform 0.2s;">
                                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                                        <h3 style="color: #2d6a4f; font-size: 18px; margin: 0;">{{item.get('title', 'Без названия')}}</h3>
                                        <span style="color: #888; font-size: 12px;">📅 {{item.get('date_formatted', item.get('date_added', 'Дата не указана'))}}</span>
                                    </div>
                                    <div>
                                        <p style="color: #555; line-height: 1.5; margin: 10px 0; font-size: 14px;">{{item.get('description', '')}}</p>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid #eee; font-size: 12px;">
                                        <span style="color: #2d6a4f; font-weight: 500;">✍️ Автор: {{item.get('author', 'Аноним')}}</span>
                                        <span style="color: #999;">ID: {{item.get('id', '')}}</span>
                                    </div>
                                </div>
                            % end
                        </div>
                    % end
                </div>
            </div>
        </div>
    </div>
</div>