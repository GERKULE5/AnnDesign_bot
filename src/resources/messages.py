class Messages:
    start_message = "Привет! Я бот-помощник графического дизайнера Анны. Чем могу помочь?"


class ButtonMessages:
    services_btn = "👋 Услуги"
    portfolio_btn = "🎨 Портфолио"
    contacts_btn = "📞 Контакты"
    submit_button = "💌 Оставить заявку"
    cancel_action = "❌ Отменить действие"

class ServicesMessages:
    logo = "Логотипы"
    style = "Фирменный стиль"
    illustrations = "Иллюстрации"

class ContactsMessages:
    contacts = "Telegram: {username} \nПочта: {email}"

class SubmitFormMessages:
    name_message = "👤 Как вас зовут?"
    incorrect_name = "❌ Пожалуйста, введите корректное имя."
    phone_message = "📱 Ваш номер телефона?"
    incorrect_phone = "❌ Пожалуйста, отправьте номер телефона."
    description_message = "📤 Кратко опишите задачу (Например: Сделать логотип для кофейни):"
    incorect_description = "❌ Пожалуйста, опишите задачу."
    final_message =  "🫶Спасибо! Ваша заявка принята. Я свяжусь с вами в ближайшее время."
    cancel_message = "❌ Действие отменено."

class AdminNotifyMessages:
    application = """
    📩 Новая заявка!\n     
    👤 Имя: {name}\n    
    📞 Телефон: {phone}\n
    💬 Описание: {description}        
    """
    type_to_user = "🖊 Написать пользователю"
    

