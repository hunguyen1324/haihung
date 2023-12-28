from TrackEval import trackeval
  # Import thư viện

# Tạo bộ đánh giá
evaluator = trackeval.Evaluator()

# Tạo cấu hình đánh giá
metrics_list = [trackeval.metrics.HOTA(), trackeval.metrics.CLEAR(), trackeval.metrics.Identity()]
eval_config = trackeval.EvaluationConfig()
# eval_config.RESULTS_FORMAT = 'mot_challenge'

# Đường dẫn tới dữ liệu theo dõi và ground truth
trackers_to_eval = ['YourTracker']
gt_folder = 'path/to/ground_truth/data'
trackers_folder = 'path/to/tracking/data'

# Thực hiện đánh giá
# results, messages = evaluator.evaluate(trackers_to_eval, eval_config, metrics_list, trackers_folder, gt_folder)
# In kết quả
# print(results)