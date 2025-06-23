from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from payments.mpesa import lipa_na_mpesa

@csrf_exempt
def mpesa_callback(request):
    data = json.loads(request.body)
    print("Callback Received:", data)
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
def initiate_stk_push(request):
    response = lipa_na_mpesa(phone='254728627678', amount=1)
    return JsonResponse(response)

# Create a logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('mpesa_callback.log')  # Log to a file
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@csrf_exempt
def mpesa_callback(request):
    try:
        data = json.loads(request.body)

        # Log the entire callback payload
        logger.info("M-Pesa Callback: %s", json.dumps(data, indent=2))
        print("📩 Callback Received:\n", json.dumps(data, indent=2))

        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

    except Exception as e:
        logger.error("❌ Error in callback: %s", str(e))
        return JsonResponse({"ResultCode": 1, "ResultDesc": "Error occurred"})