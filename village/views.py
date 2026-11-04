from django.shortcuts import render
from .models import Notice, Complaint, GalleryImage, ImportantContact, VillageInfo
from .forms import ComplaintForm, ComplaintTrackForm


def home(request):
    notices = Notice.objects.all()[:5]
    emergency_contacts = ImportantContact.objects.filter(is_emergency=True)[:4]
    all_contacts = ImportantContact.objects.filter(is_emergency=False)[:4]
    gallery = GalleryImage.objects.all()[:4]
    info_items = VillageInfo.objects.all()[:6]

    context = {
        "notices": notices,
        "emergency_contacts": emergency_contacts,
        "all_contacts": all_contacts,
        "gallery": gallery,
        "info_items": info_items,
        "total_complaints": Complaint.objects.count(),
        "pending_complaints": Complaint.objects.filter(status="Pending").count(),
        "in_progress_complaints": Complaint.objects.filter(status="In Progress").count(),
        "resolved_complaints": Complaint.objects.filter(status="Resolved").count(),
    }
    return render(request, "village/home.html", context)


def gramseva(request):
    """
    Dedicated Citizen Services section:
    - जन्म प्रमाणपत्र माहिती
    - मृत्यू प्रमाणपत्र माहिती
    - रहिवासी प्रमाणपत्र माहिती
    - घरपट्टी माहिती
    - पाणीपट्टी माहिती
    - ग्रामपंचायत अर्ज व नमुने
    - आवश्यक कागदपत्रे
    - ग्रामपंचायत कार्यालयीन वेळ व संपर्क
    """
    services_list = [
        {
            "id": "birth",
            "name": "जन्म प्रमाणपत्र (Birth Certificate)",
            "icon": "👶",
            "category": "नागरी दाखले",
            "is_online": False,
            "badge": "माहिती व अर्ज मार्गदर्शन",
            "time_limit": "जन्म झाल्यापासून २१ दिवसांच्या आत विनामूल्य नोंदणी",
            "description": "गावामध्ये झालेल्या जन्माची अधिकृत नोंद ग्रामपंचायत दप्तरी करून जन्म दाखला दिला जातो.",
            "documents": [
                "हॉस्पिटल/प्राथमिक आरोग्य केंद्राचा जन्म अहवाल (डिस्चार्ज कार्ड)",
                "आई व वडिलांचे आधार कार्ड",
                "आई-वडिलांचे रेशन कार्ड",
                "विवाह नोंदणी प्रमाणपत्र (लागू असल्यास)",
            ],
            "process": "हॉस्पिटलचा दाखला व पालकांचे आधार कार्ड घेऊन ग्रामपंचायत कार्यालयात ग्रामसेवक यांच्याकडे अर्ज सादर करावा. २१ दिवसांनंतर विलंब नोंदणीसाठी तहसीलदारांचा आदेश आवश्यक असतो.",
            "portal_url": "https://aaplesarkar.mahaonline.gov.in/",
            "portal_name": "आपले सरकार पोर्टल",
        },
        {
            "id": "death",
            "name": "मृत्यू प्रमाणपत्र (Death Certificate)",
            "icon": "🕊️",
            "category": "नागरी दाखले",
            "is_online": False,
            "badge": "माहिती व अर्ज मार्गदर्शन",
            "time_limit": "मृत्यू झाल्यापासून २१ दिवसांच्या आत विनामूल्य नोंदणी",
            "description": "गावातील मयताची कायदेशीर नोंद करून वारसांना अधिकृत मृत्यू दाखला दिला जातो.",
            "documents": [
                "वैद्यकीय अधिकाऱ्यांचे मृत्यू प्रमाणपत्र किंवा स्मशानभूमी पावती",
                "मृत व्यक्तीचे आधार कार्ड",
                "अर्जदाराचे आधार कार्ड व मृत व्यक्तीशी संबंधाचा पुरावा",
                "रेशन कार्ड",
            ],
            "process": "कागदपत्रांसह ग्रामपंचायत कार्यालयात अर्ज करावा. अधिकृत नोंदणीनंतर ग्रामसेवक यांच्या स्वाक्षरीने दाखला दिला जातो.",
            "portal_url": "https://aaplesarkar.mahaonline.gov.in/",
            "portal_name": "आपले सरकार पोर्टल",
        },
        {
            "id": "residence",
            "name": "रहिवासी दाखला (Residence Certificate)",
            "icon": "🏡",
            "category": "नागरी दाखले",
            "is_online": False,
            "badge": "ग्रामपंचायत सेवा",
            "time_limit": "२ ते ३ कार्यालयीन दिवस",
            "description": "शालेय प्रवेश, नोकरी व शासकीय योजनांसाठी तऱ्हाडी गावचा कायमस्वरूपी रहिवासी असल्याचा दाखला.",
            "documents": [
                "अर्जदाराचे आधार कार्ड",
                "कुटुंबाचे रेशन कार्ड",
                "घरपट्टी पावती किंवा चालू लाइट बिल",
                "पासपोर्ट आकाराचा फोटो",
            ],
            "process": "ग्रामपंचायत विहित नमुन्यातील अर्ज भरून सरपंच किंवा ग्रामसेवक यांच्या सही-शिक्क्याने दाखला मिळवावा.",
            "portal_url": "https://aaplesarkar.mahaonline.gov.in/",
            "portal_name": "आपले सरकार पोर्टल",
        },
        {
            "id": "property_tax",
            "name": "घरपट्टी आकारणी व पावती (Property Tax)",
            "icon": "🏠",
            "category": "कर व महसूल",
            "is_online": False,
            "badge": "थेट ग्रामपंचायत कार्यालय",
            "time_limit": "तातडीने (पावतीसह)",
            "description": "गावातील घर, गाळा व इमारतींचे ग्रामपंचायत नमूना ८ नुसार मूल्यांकन व वार्षिक घरपट्टी आकारणी.",
            "documents": [
                "मागील वर्षाची घरपट्टी पावती",
                "मालमत्ता धारकाचे आधार कार्ड",
                "नवीन बांधकामासाठी बांधकाम परवानगी व जागेचा दाखला",
            ],
            "process": "ग्रामपंचायत कार्यालयात जाऊन घरपट्टी भरून अधिकृत शासकीय पावती मिळवावी. दरवर्षी नियमित कर भरून गावादिकासात सहकार्य करावे.",
            "portal_url": "",
            "portal_name": "",
        },
        {
            "id": "water_tax",
            "name": "पाणीपट्टी आकारणी व नळ जोडणी (Water Supply)",
            "icon": "💧",
            "category": "कर व महसूल",
            "is_online": False,
            "badge": "थेट ग्रामपंचायत कार्यालय",
            "time_limit": "तातडीने / नळ जोडणी ५ ते ७ दिवस",
            "description": "जल जीवन मिशन अंतर्गत घरोघरी शुद्ध नळ पाणीपुरवठ्याची वार्षिक पाणीपट्टी व नवीन नळ जोडणी अर्ज.",
            "documents": [
                "घरपट्टी चालू वर्षाची पावती",
                "आधार कार्ड व रेशन कार्ड",
                "नवीन नळ जोडणीसाठी विहित नमुन्यातील अर्ज",
            ],
            "process": "पाणीपुरवठा कर्मचारी किंवा ग्रामपंचायत लिपिक यांच्याकडे पाणीपट्टी भरून पावती घ्यावी. नवीन नळ जोडणीसाठी ग्रामसभेची/सरपंचांची मंजुरी लागते.",
            "portal_url": "",
            "portal_name": "",
        },
        {
            "id": "complaint",
            "name": "ऑनलाइन तक्रार निवारण (Online Grievance)",
            "icon": "📝",
            "category": "डिजिटल सेवा",
            "is_online": True,
            "badge": "थेट ऑनलाइन सुविधा",
            "time_limit": "७ ते १५ कार्यालयीन दिवस",
            "description": "पाणी, रस्ता, वीज, स्वच्छता या समस्यांची तक्रार डिजिटल पद्धतीने थेट ग्रामपंचायतीकडे नोंदवा व ट्रॅक करा.",
            "documents": [
                "तक्रारदाराचे नाव व १० अंकी मोबाइल नंबर",
                "समस्येचे ठिकाण व सविस्तर माहिती",
            ],
            "process": "या वेबसाइटवर 'ऑनलाइन तक्रार' मेनूवर जाऊन फॉर्म भरा. मिळालेल्या १२ अंकी Complaint ID द्वारे सद्यस्थिती तपासा.",
            "portal_url": "/complaints/",
            "portal_name": "ऑनलाइन तक्रार नोंदवा →",
        },
    ]

    forms_list = [
        {"title": "नमुना ८ (मालमत्ता नोंद उतारा अर्ज)", "desc": "घर किंवा जागेचा अधिकृत नमुना ८ उतारा मिळवण्यासाठी अर्ज.", "icon": "📄"},
        {"title": "नवीन नळ जोडणी मागणी अर्ज", "desc": "घरगुती नळ जोडणीसाठी ग्रामपंचायतीचा अधिकृत अर्ज नमुना.", "icon": "💧"},
        {"title": "बांधकाम परवानगी मागणी अर्ज", "desc": "गावात नवीन घर किंवा बांधकाम करण्यासाठी पूर्वपरवानगी अर्ज.", "icon": "🏗️"},
        {"title": "ना हरकत प्रमाणपत्र (NOC) अर्ज", "desc": "वीज मीटर, उद्योग किंवा इतर कामांसाठी ग्रामपंचायत NOC.", "icon": "📜"},
        {"title": "दारिद्र्य रेषेखालील (BPL) दाखला अर्ज", "desc": "शासकीय योजनांसाठी BPL यादीत नाव असल्याचा दाखला अर्ज.", "icon": "📋"},
    ]

    office_info = {
        "timing": "सकाळी १०:०० ते सायंकाळी ५:४५ (सोमवार ते शनिवार)",
        "holiday": "रविवार, २ रा व ४ था शनिवार, तसेच शासकीय सुट्ट्या",
        "address": "ग्रामपंचायत कार्यालय, मु. पो. तऱ्हाडी त.त., तालुका शिरपूर, जिल्हा धुळे — ४२५४०५",
        "email": "tarhadigp@gmail.com",
    }

    return render(request, "village/gramseva.html", {
        "services": services_list,
        "forms": forms_list,
        "office_info": office_info,
    })


def about(request):
    info_items = VillageInfo.objects.all()
    contacts = ImportantContact.objects.all().order_by("order")

    return render(request, "village/about.html", {
        "info_items": info_items,
        "contacts": contacts,
    })


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "village/gallery.html", {"images": images})


def contacts(request):
    emergency = ImportantContact.objects.filter(is_emergency=True).order_by("order")
    regular = ImportantContact.objects.filter(is_emergency=False).order_by("order")
    return render(request, "village/contacts.html", {
        "emergency": emergency,
        "regular": regular,
    })


def schemes(request):
    scheme_list = [
        # Central Government
        {
            "name": "प्रधानमंत्री किसान सन्मान निधी (PM-KISAN)",
            "gov_type": "केंद्र शासन",
            "category": "शेतकरी",
            "icon": "🌾",
            "description": "सर्व पात्र शेतकरी कुटुंबांना दरवर्षी ₹६,००० ची थेट आर्थिक मदत (३ समान हप्त्यांमध्ये).",
            "eligibility": "स्वतःच्या नावावर शेती असणारे अल्प व अत्यल्प भूधारक शेतकरी (e-KYC व आधार लिंक आवश्यक).",
            "documents": "७/१२ व ८-अ उतारा, आधार कार्ड, बँक पासबुक, e-KYC पावती.",
            "instructions": "अधिकृत PM-Kisan पोर्टलवर जाऊन New Farmer Registration मधून नोंदणी करा किंवा जवळच्या CSC केंद्रात जा.",
            "url": "https://pmkisan.gov.in/",
        },
        {
            "name": "प्रधानमंत्री आवास योजना - ग्रामीण (PMAY-G)",
            "gov_type": "केंद्र शासन",
            "category": "घरकुल",
            "icon": "🏠",
            "description": "ग्रामीण भागातील बेघर व कच्च्या घरात राहणाऱ्या कुटुंबांना पक्के घर बांधण्यासाठी ₹१,२०,००० अनुदान.",
            "eligibility": "SECC २०११ यादीतील किंवा आवास प्लस यादीतील पात्र बेघर/कच्चे घर असलेली कुटुंबे.",
            "documents": "आधार कार्ड, जॉब कार्ड (मनरेगा), बँक पासबुक, जागेचा दाखला, कुटुंबाचा फोटो.",
            "instructions": "ग्रामसभेत नाव मंजुरीनंतर ग्रामसेवक किंवा पंचायत समितीमार्फत अर्ज ऑनलाइन अपलोड होतो.",
            "url": "https://pmayg.nic.in/",
        },
        {
            "name": "आयुष्मान भारत - PMJAY (जन आरोग्य योजना)",
            "gov_type": "केंद्र शासन",
            "category": "आरोग्य",
            "icon": "🏥",
            "description": "पात्र कुटुंबांना दरवर्षी ₹५ लाखांपर्यंत मोफत व कॅशलेस वैद्यकीय उपचारांची सुविधा.",
            "eligibility": "SECC यादीतील पात्र कुटुंबे, रेशन कार्ड धारक नागरिक.",
            "documents": "आधार कार्ड, रेशन कार्ड (पिवळे/केशरी), मोबाइल नंबर.",
            "instructions": "जवळच्या सेतू केंद्र, ग्रामीण रुग्णालय किंवा अधिकृत पोर्टलवर जाऊन आयुष्मान कार्ड डाउनलोड करा.",
            "url": "https://beneficiary.nha.gov.in/",
        },
        {
            "name": "जल जीवन मिशन (हर घर जल)",
            "gov_type": "केंद्र शासन",
            "category": "पाणीपुरवठा",
            "icon": "💧",
            "description": "प्रत्येक ग्रामीण कुटुंबाला घरगुती नळ जोडणीद्वारे शुद्ध व पुरेसे पिण्याचे पाणी.",
            "eligibility": "गावातील सर्व ग्रामीण कुटुंबे.",
            "documents": "घरपट्टी पावती, आधार कार्ड.",
            "instructions": "ग्रामपंचायत कार्यालयात नळ जोडणीचा अर्ज सादर करावा.",
            "url": "https://jaljeevanmission.gov.in/",
        },
        {
            "name": "स्वच्छ भारत मिशन - ग्रामीण (शौचालय अनुदान)",
            "gov_type": "केंद्र शासन",
            "category": "स्वच्छता",
            "icon": "🚿",
            "description": "घरी वैयक्तिक शौचालय बांधण्यासाठी पात्र कुटुंबांना ₹१२,००० चे थेट शासकीय अनुदान.",
            "eligibility": "ज्या कुटुंबाकडे शौचालय उपलब्ध नाही अशी ग्रामीण कुटुंबे.",
            "documents": "आधार कार्ड, बँक पासबुक, जागेचा पुरावा, बांधकामाचा फोटो.",
            "instructions": "ग्रामपंचायतीमार्फत अर्ज करून जिओ-टॅगिंगनंतर अनुदान खात्यात जमा होते.",
            "url": "https://sbm.gov.in/",
        },
        # Maharashtra Government
        {
            "name": "नमो शेतकरी महासन्मान निधी योजना",
            "gov_type": "महाराष्ट्र शासन",
            "category": "शेतकरी",
            "icon": "💰",
            "description": "PM-Kisan सोबतच महाराष्ट्र शासनाकडून अतिरिक्त ₹६,००० दरवर्षी (एकूण ₹१२,००० लाभ).",
            "eligibility": "केंद्र शासनाच्या PM-Kisan योजनेचा लाभ घेणारे महाराष्ट्रातील सर्व पात्र शेतकरी.",
            "documents": "PM-Kisan नोंदणी क्रमांक, आधार लिंक बँक खाते.",
            "instructions": "PM-Kisan लाभार्थींना स्वतंत्र अर्ज न करता थेट खात्यात लाभ मिळतो.",
            "url": "https://mahadbt.maharashtra.gov.in/",
        },
        {
            "name": "महाडीबीटी कृषी यांत्रिकीकरण व अवजारे अनुदान",
            "gov_type": "महाराष्ट्र शासन",
            "category": "शेतकरी",
            "icon": "🚜",
            "description": "ट्रॅक्टर, रोटाव्हेटर, पेरणी यंत्र, ताडपत्री व इतर कृषी अवजारांवर ५०% ते ७५% अनुदान.",
            "eligibility": "महाराष्ट्रातील शेतकरी (अनुसूचित जाती, जमाती व महिला शेतकऱ्यांना प्राधान्य).",
            "documents": "७/१२, ८-अ, आधार कार्ड, बँक पासबुक, खरेदी कोटेशन.",
            "instructions": "MahaDBT पोर्टलवर 'शेतकरी योजना' मध्ये ऑनलाइन अर्ज करून लॉटरी पद्धतीची प्रतीक्षा करावी.",
            "url": "https://mahadbt.maharashtra.gov.in/",
        },
        {
            "name": "लेक लाडकी योजना",
            "gov_type": "महाराष्ट्र शासन",
            "category": "महिला व बाल",
            "icon": "👧",
            "description": "मुलींच्या जन्मापासून ते १८ वर्षे वयापर्यंत टप्प्याटप्प्याने एकूण ₹१,०१,००० ची आर्थिक मदत.",
            "eligibility": "पिवळे व केशरी रेशन कार्ड धारक कुटुंबात १ एप्रिल २०२३ नंतर जन्मलेल्या मुली.",
            "documents": "मुलीचा जन्म दाखला, आई-वडिलांचे आधार कार्ड, रेशन कार्ड, बँक पासबुक.",
            "instructions": "अंगणवाडी सेविका किंवा ग्रामपंचायत कार्यालयामार्फत महिला व बालविकास विभागाकडे अर्ज करावा.",
            "url": "https://womenchild.maharashtra.gov.in/",
        },
        {
            "name": "संजय गांधी निराधार अनुदान योजना",
            "gov_type": "महाराष्ट्र शासन",
            "category": "सामाजिक न्याय",
            "icon": "🤝",
            "description": "निराधार वृद्ध, दिव्यांग, विधवा व अनाथ व्यक्तींना दरमहा ₹१,५०० ची पेन्शन मदत.",
            "eligibility": "६५ वर्षांवरील निराधार, अपंगत्व ४०% पेक्षा जास्त असणारे, वार्षिक उत्पन्न मर्यादा ₹५०,००० आत.",
            "documents": "वयाचा पुरावा, उत्पन्नाचा दाखला (तहसीलदार), दिव्यांग दाखला (लागू असल्यास), आधार कार्ड.",
            "instructions": "तहसील कार्यालयात किंवा सेतू केंद्रात संजय गांधी निराधार योजनेचा अर्ज सादर करावा.",
            "url": "https://sanjaygandhi.maharashtra.gov.in/",
        },
        {
            "name": "राष्ट्रीय अन्न सुरक्षा योजना (स्वस्त धान्य)",
            "gov_type": "केंद्र व राज्य शासन",
            "category": "अन्न सुरक्षा",
            "icon": "🍚",
            "description": "अंत्योदय व प्राधान्य कुटुंब शिधापत्रिका धारकांना मोफत गहू, तांदूळ व भरडधान्य वाटप.",
            "eligibility": "पिवळे व पात्र केशरी रेशन कार्ड धारक कुटुंबे (RCMS प्रणालीत नोंद).",
            "documents": "आधार लिंक डिजिटल रेशन कार्ड.",
            "instructions": "गावातील अधिकृत स्वस्त धान्य दुकानात ई-पॉस मशीनवर अंगठा लावून धान्य घ्यावे.",
            "url": "https://mahaepos.gov.in/",
        },
    ]

    return render(
        request,
        "village/schemes.html",
        {"schemes": scheme_list},
    )


def shetkari_yojana(request):
    """
    Dedicated Farmer Section:
    - पीक विमा (PMFBY)
    - कृषी अनुदान (MahaDBT)
    - सिंचन योजना (सूक्ष्म सिंचन ठिबक व तुषार)
    - कृषी उपकरण अनुदान
    - शेतकरी सन्मान योजना
    - कृषी विभागाच्या सूचना व मार्गदर्शन
    """
    farmer_schemes = [
        {
            "title": "प्रधानमंत्री पीक विमा योजना (१ रुपयात पीक विमा)",
            "icon": "🛡️",
            "category": "पीक विमा संरक्षण",
            "desc": "नैसर्गिक आपत्ती, दुष्काळ, अतिवृष्टी किंवा कीड-रोगामुळे पिकांचे नुकसान झाल्यास शेतकऱ्यांना भरपाई.",
            "benefit": "केवळ ₹१ भरून विमा नोंदणी. उर्वरित विमा हप्ता शासन भरते.",
            "crops": "खरीप (कापूस, मका, सोयाबीन, बाजरी) व रब्बी (गहू, हरभरा, ज्वारी).",
            "url": "https://pmfby.gov.in/",
            "portal": "PMFBY Portal ↗",
        },
        {
            "title": "मुख्यमंत्री शाश्वत कृषी सिंचन योजना (ठिबक व तुषार)",
            "icon": "💧",
            "category": "सिंचन सुविधा",
            "desc": "पाण्याचा योग्य वापर करण्यासाठी ठिबक सिंचन व तुषार सिंचन संचावर ७५% ते ८०% पर्यंत थेट सबसिडी.",
            "benefit": "अल्प व अत्यल्प भूधारकांना ८०% आणि इतर शेतकऱ्यांना ७५% अनुदान थेट खात्यात.",
            "crops": "कापूस, फळबागा, भाजीपाला, मका, ऊस आदी पिकांसाठी.",
            "url": "https://mahadbt.maharashtra.gov.in/",
            "portal": "महाडीबीटी सिंचन अर्ज ↗",
        },
        {
            "title": "कृषी यांत्रिकीकरण योजना (ट्रॅक्टर व अवजारे अनुदान)",
            "icon": "🚜",
            "category": "यंत्रसामग्री",
            "desc": "शेतकामांचा वेग वाढवण्यासाठी ट्रॅक्टर, पॉवर टिलर, रोटाव्हेटर, मळणी यंत्र खरेदीसाठी भरघोस शासकीय अनुदान.",
            "benefit": "अनुदान मर्यादा ₹१ लाख ते ₹१.२५ लाख (ट्रॅक्टरसाठी) किंवा अवजाराच्या किमतीच्या ५०%.",
            "crops": "सर्व शेतकरी बांधवांसाठी.",
            "url": "https://mahadbt.maharashtra.gov.in/",
            "portal": "महाडीबीटी अवजारे अर्ज ↗",
        },
        {
            "title": "नमो शेतकरी + PM-Kisan सन्मान निधी",
            "icon": "🌾",
            "category": "आर्थिक पाठबळ",
            "desc": "केंद्र व राज्य शासनाकडून दरवर्षी मिळून ₹१२,००० चा थेट आर्थिक लाभ (प्रत्येक ४ महिन्यांनी ₹४,००० खात्यात).",
            "benefit": "बियाणे, खते व शेती खर्चासाठी थेट बँक खात्यात सन्मान निधी.",
            "crops": "सर्व शेतजमीन धारक कुटुंबे.",
            "url": "https://pmkisan.gov.in/",
            "portal": "PM-Kisan पोर्टल ↗",
        },
        {
            "title": "मृदा आरोग्य पत्रिका (Soil Health Card)",
            "icon": "🧪",
            "category": "जमीन आरोग्य तपासणी",
            "desc": "आपल्या शेतातील मातीचे सॅम्पल तपासून खतांचा समतोल वापर कसा करावा याबाबत कृषी विभागाचे मोफत मार्गदर्शन.",
            "benefit": "खतांचा नाहक खर्च वाचतो आणि जमिनीची सुपीकता दीर्घकाळ टिकून राहते.",
            "crops": "सर्व पिकांसाठी.",
            "url": "https://soilhealth.dac.gov.in/",
            "portal": "Soil Health Portal ↗",
        },
        {
            "title": "मागेल त्याला शेततळे योजना",
            "icon": "🏊",
            "category": "जलसंधारण",
            "desc": "पावसाचे पाणी साठवून संरक्षित सिंचनाची व्यवस्था करण्यासाठी शेततळे खोदाई व प्लास्टिक अस्तरसाठी अनुदान.",
            "benefit": "प्लॅस्टिक अस्तरीकरणासह शेततळ्यासाठी ₹७५,००० पर्यंत थेट शासकीय अनुदान.",
            "crops": "बागायती व कोरडवाहू शेती.",
            "url": "https://mahadbt.maharashtra.gov.in/",
            "portal": "महाडीबीटी शेततळे ↗",
        },
    ]

    agri_advisory = [
        {
            "crop": "कापूस (Cotton)",
            "tip": "बोंडअळीच्या नियंत्रणासाठी कामगंध सापळे लावा. पाण्याचा निचरा योग्य राखा व फवारणी करताना संरक्षक किट वापरा.",
        },
        {
            "crop": "मका (Maize)",
            "tip": "लष्करी अळीच्या प्रादुर्भावावर सुरुवातीलाच निंबोळी अर्काची फवारणी करा. युरियाचा समतोल वापर ठेवा.",
        },
        {
            "crop": "केळी व पपई (Horticulture)",
            "tip": "थंडीच्या मोसमात पानांचे संरक्षण करण्यासाठी बागेभोवती शेवरी/हवाबंद कुंपण लावा. सूक्ष्म अन्नद्रव्यांचा डोस द्या.",
        },
    ]

    return render(
        request,
        "village/shetkari_yojana.html",
        {
            "schemes": farmer_schemes,
            "advisory": agri_advisory,
        },
    )


def complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            saved_complaint = Complaint.objects.create(
                name=form.cleaned_data['name'],
                mobile=form.cleaned_data['mobile'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
            )
            return render(
                request,
                "village/complaint.html",
                {"saved_complaint": saved_complaint},
            )
        else:
            return render(
                request,
                "village/complaint.html",
                {"form": form, "error": "सर्व माहिती योग्य पद्धतीने भरा."},
            )

    form = ComplaintForm()
    return render(request, "village/complaint.html", {"form": form})


def complaint_track(request):
    result = None
    error = None
    form = ComplaintTrackForm()

    if request.method == "POST":
        form = ComplaintTrackForm(request.POST)
        if form.is_valid():
            complaint_id = form.cleaned_data['complaint_id'].strip().upper()
            mobile = form.cleaned_data['mobile']

            result = Complaint.objects.filter(
                complaint_id=complaint_id,
                mobile=mobile,
            ).first()

            if result is None:
                error = "तक्रार सापडली नाही. Complaint ID आणि मोबाइल नंबर तपासा."
        else:
            error = "योग्य Complaint ID आणि 10 अंकी मोबाइल नंबर भरा."

    return render(
        request,
        "village/complaint_track.html",
        {"result": result, "error": error, "form": form},
    )


def custom_404(request, exception):
    return render(request, "village/404.html", status=404)