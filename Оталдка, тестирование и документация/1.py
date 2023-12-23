import cProfile
import pstats
from functions_to_profile import load_files, read_database, get_id, get_user_data, generate_words

TASK_FUNCTIONS_ORDER = ['load_files', 'read_database', 'get_id', 'get_user_data', 'generate_words']

profiler = cProfile.Profile()
profiler.enable()
load_files()
read_database()
get_id()
get_user_data()
generate_words()
profiler.disable()
profiler.create_stats()
statistic = pstats.Stats(profiler)
statistic = statistic.get_stats_profile()
all_time = statistic.total_tt
for function in TASK_FUNCTIONS_ORDER:
    function_time = statistic.func_profiles[function].cumtime
    function_per = function_time / all_time * 100
    print(f"{function_time:.4f}: {int(function_per)}%")
    