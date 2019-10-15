from django.shortcuts import render
from django.http import HttpResponse
from .extras import get_image_data, dump_json, preprocess_malaria, preprocess_skin_cancer
from tensorflow.keras.models import load_model

#malaria_model = load_model("models\malaria.h5")
print("Loaded Malaria Model")

#skin_cancer_model = load_model("models\skin_cancer.h5")
print("Loaded Skin Cancer Model")

# Create your views here.
def index(request):
    return render(request, "api-index.html")

def malaria(request):
    try:
        img_url = request.GET.get("img_url", None)

        if img_url:
            img_data = get_image_data(img_url)
            img_data = preprocess_malaria(img_data)
            test_result = malaria_model.predict([[img_data]])
            confidence_score = test_result[0][test_result.argmax()] * 100

            if test_result.argmax() == 0:
                test_message = "Malaria Negative with {:.2f}% confidence".format(confidence_score)
                result = "Negative"
            else:
                test_message = "Malaria Positive with {:.2f}% confidence".format(confidence_score)
                result = "Positive"
        else:
            return HttpResponse(dump_json({"success": False, "test_type": "malaria", "error": "No image url was provided", "message": None}))

        return HttpResponse(dump_json({"success": True, "error": None, "test_type": "malaria", "message": test_message, "result": result, "confidence": confidence_score}))
    except Exception as e:
        return HttpResponse(dump_json({"success": False, "error": "An error occured during the test", "test_type": "malaria", "message": None}))

def skin_cancer(request):
    try:
        img_url = request.GET.get("img_url", None)

        if img_url:
            img_data = get_image_data(img_url)
            img_data = preprocess_skin_cancer(img_data)
            test_result = skin_cancer_model.predict([[img_data]])[0][0]

            if round(test_result) == 0:
                confidence_score = (1 - test_result) * 100
                test_message = "Detected Benign Cancer with {:.2f}% confidence".format(confidence_score)
                result = "Benign"
            else:
                confidence_score = test_result * 100
                test_message = "Detected Malignant Cancer with {:.2f}% confidence".format(confidence_score)
                result = "Malignant"
        else:
            return HttpResponse(dump_json({"success": False, "test_type": "skin_cancer", "error": "No image url was provided", "message": None}))

        return HttpResponse(dump_json({"success": True, "error": None, "test_type": "skin_cancer", "message": test_message, "result": result, "confidence": confidence_score}))
    except Exception as e:
        return HttpResponse(dump_json({"success": False, "error": "An error occured during the test", "test_type": "skin_cancer", "message": None}))
