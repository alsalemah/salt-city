from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

landmarks = [
    {
        "id": 1,
        "name": "متحف السلط الإقليمي",
        "category": "متاحف",
        "description": "يضم المتحف مقتنيات أثرية نادرة تروي تاريخ المنطقة من العصور البرونزية حتى العصر العثماني. يقع في مبنى عثماني أصيل يعود للقرن التاسع عشر.",
        "year": "١٨٩٠",
        "icon": "🏛️",
        "image": "https://images.unsplash.com/photo-1564399263809-d2e776baf7df?w=900&q=85",
        "facts": ["أُسِّس عام ١٩٩٧", "يضم أكثر من ٥٠٠٠ قطعة أثرية", "يُقام فيه معارض سنوية"]
    },
    {
        "id": 2,
        "name": "الحمام العثماني",
        "category": "تراث",
        "description": "حمام تاريخي يعود للحقبة العثمانية، بُني بالحجر الأصفر الجيري المميز لمدينة السلط. يمثّل نموذجاً فريداً للعمارة العثمانية في الأردن.",
        "year": "١٨٦٧",
        "icon": "🕌",
        "image": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=900&q=85",
        "facts": ["بُني في القرن التاسع عشر", "تحفة معمارية عثمانية", "مدرج على قائمة التراث العالمي"]
    },
    {
        "id": 3,
        "name": "كنيسة الروم الأرثوذكس",
        "category": "دور عبادة",
        "description": "من أعرق الكنائس في الأردن، شيدت بالحجر الرملي الأصفر وتتميز بأجراسها الرنانة وفسيفسائها الجميلة. تعكس التعايش المسيحي الإسلامي العريق في المدينة.",
        "year": "١٨٩٩",
        "icon": "⛪",
        "image": "https://images.unsplash.com/photo-1548625149-720fb4f57c5c?w=900&q=85",
        "facts": ["بُنيت عام ١٨٩٩م", "تحفة في الفسيفساء البيزنطية", "رمز التعايش في السلط"]
    },
    {
        "id": 4,
        "name": "مسجد أبو دربالة",
        "category": "دور عبادة",
        "description": "أحد أقدم مساجد السلط وأجملها، يتميز بمئذنته الشامخة ونقوشه الإسلامية الدقيقة. يُعدّ مركزاً روحياً وثقافياً لأبناء المدينة.",
        "year": "١٨٥٠",
        "icon": "🕌",
        "image": "https://images.unsplash.com/photo-1585507252242-11fe632c26e8?w=900&q=85",
        "facts": ["من أقدم مساجد السلط", "مئذنة عثمانية أصيلة", "مركز ثقافي وتعليمي"]
    },
    {
        "id": 5,
        "name": "منطقة البلد التاريخية",
        "category": "معالم",
        "description": "قلب السلط النابض — ازقة مرصوفة بالحجر القديم، وبيوت عثمانية ذات نوافذ بيضاء وقناطر حجرية. هنا تسير بين صفحات التاريخ الحي.",
        "year": "١٧٠٠",
        "icon": "🏘️",
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&q=85",
        "facts": ["مدرجة على قائمة اليونسكو ٢٠٢١", "أكثر من ٢٠٠ مبنى تاريخي", "مركز ثقافي حي"]
    },
    {
        "id": 6,
        "name": "متحف الفن الحديث",
        "category": "متاحف",
        "description": "مساحة إبداعية تجمع أعمال فنانين أردنيين وعرب في فضاء معماري حديث يكتنز بتراث السلط العريق. جسرٌ بين الأصالة والمعاصرة.",
        "year": "٢٠٠٥",
        "icon": "🎨",
        "image": "https://images.unsplash.com/photo-1574182245530-967d9b3831af?w=900&q=85",
        "facts": ["أكثر من ٣٠٠ عمل فني", "يستضيف فعاليات شهرية", "يدعم الفنانين الشباب"]
    }
]

gallery = [
    {
        "id": 1,
        "title": "الحجر الأصفر .. روح السلط",
        "caption": "المباني العثمانية بحجرها الجيري الذهبي تُضفي على السلط طابعها الفريد",
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&q=85"
    },
    {
        "id": 2,
        "title": "ازقة التاريخ",
        "caption": "أزقة البلد القديم تحكي قصص الأجداد وتنبض بالحياة حتى اليوم",
        "image": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=1200&q=85"
    },
    {
        "id": 3,
        "title": "ليل السلط",
        "caption": "المدينة تزداد جمالاً حين تُضيء أنوارها الدافئة على المباني الأثرية",
        "image": "https://images.unsplash.com/photo-1548625149-720fb4f57c5c?w=1200&q=85"
    },
    {
        "id": 4,
        "title": "التعايش .. إرث خالد",
        "caption": "مئذنة وجرس كنيسة تتجاوران — رمز التسامح الذي اشتهرت به السلط",
        "image": "https://images.unsplash.com/photo-1585507252242-11fe632c26e8?w=1200&q=85"
    }
]

stats = [
    {"label": "سنة التأسيس", "value": "٣٠٠٠ ق.م"},
    {"label": "عدد المواقع التراثية", "value": "+٢٠٠"},
    {"label": "تُصنَّف عالمياً", "value": "يونسكو ٢٠٢١"},
    {"label": "المساحة", "value": "٤٠٧ كم²"}
]

categories = ["الكل", "متاحف", "تراث", "دور عبادة", "معالم"]

@app.route('/')
def index():
    return render_template('index.html',
        landmarks=landmarks,
        gallery=gallery,
        stats=stats,
        categories=categories
    )

@app.route('/api/landmarks')
def api_landmarks():
    cat = request.args.get('category', 'الكل')
    if cat == 'الكل':
        return jsonify(landmarks)
    return jsonify([l for l in landmarks if l['category'] == cat])

@app.route('/api/landmark/<int:lid>')
def api_landmark(lid):
    item = next((l for l in landmarks if l['id'] == lid), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
