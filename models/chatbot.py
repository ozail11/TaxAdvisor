import random
import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

responses = {
    "السلام عليكم": "عليكم السلام ورحمة الله  كيف يمكنني  مساعدتك؟",
    "ما هي الضرائب؟": "الضرائب هي رسوم مالية تفرضها الحكومة على الأفراد والشركات لتمويل الخدمات العامة.",
    "ما هي ضريبة القيمة المضافة؟": "ضريبة القيمة المضافة (VAT) هي ضريبة تفرض على السلع والخدمات في كل مرحلة من مراحل الإنتاج أو التوزيع.",
    "كيف أحسب ضريبة الدخل؟": "تحسب ضريبة الدخل بناءً على الدخل السنوي وفقًا للفئات الضريبية المحددة من قبل الحكومة.",
    "ما هي ضريبة الشركات؟": "ضريبة الشركات هي ضريبة تفرض على أرباح الشركات التجارية التي يتم تحقيقها من خلال الأنشطة التجارية.",
    "كيف يتم تحديد معدل ضريبة الدخل؟": "معدل ضريبة الدخل يعتمد على شريحة الدخل التي يحققها الفرد أو الشركة، ويتم تحديده وفقًا لقوانين الضريبة المحلية.",
    "ما هي ضريبة الميراث؟": "ضريبة الميراث هي ضريبة تفرض على الممتلكات التي يتم توريثها بعد وفاة شخص ما.",
    "كيف يمكنني تقديم إقرار ضريبي؟": "يمكنك تقديم إقرار ضريبي إلكترونيًا من خلال موقع الهيئة الضريبية أو من خلال التقديم الورقي في المكاتب المعتمدة.",
    "ما هو الإقرار الضريبي؟": "الإقرار الضريبي هو وثيقة تقدمها الشركات أو الأفراد إلى السلطات الضريبية لإظهار دخلهم ونفقاتهم والضرائب المستحقة عليهم.",
}

greetings = ["مرحبا", "أهلاً", "صباح الخير", "مساء الخير"]

def handle_greetings(user_query):
    if any(greeting in user_query for greeting in greetings):
        return "مرحباً! كيف يمكنني مساعدتك اليوم؟"
    return None

def handle_time(user_query):
    if "الوقت" in user_query or "كم الساعة" in user_query:
        now = datetime.datetime.now()
        return f"الوقت الحالي هو {now.strftime('%H:%M:%S')}"
    return None

def handle_weather(user_query):
    if "الطقس" in user_query or "الجو" in user_query:
        return "الطقس اليوم جميل، السماء صافية!"
    return None

def get_response(user_query):
    user_query = user_query.lower()

    response = handle_greetings(user_query)
    if response:
        return response

    response = handle_time(user_query)
    if response:
        return response

    response = handle_weather(user_query)
    if response:
        return response

    matching_responses = [answer for question, answer in responses.items() if question in user_query]
    
    if matching_responses:
        return " \n".join(matching_responses)

    default_responses = [
        "عذراً، لم أفهم سؤالك. من فضلك حاول مرة أخرى.",
        "هل يمكنك توضيح السؤال أكثر؟",
        "عذراً، ليس لدي إجابة على هذا السؤال الآن."
    ]
    return random.choice(default_responses)
