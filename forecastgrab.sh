wget -S -O news2.jpg http://cw2.trb.com/includes/webcams/kwgn/Web%20Weekly%20Planner.JPG
mv news2.jpg news2_$(date +%Y%m%d-%H%M).jpg

wget -S -O fox.jpg http://media.myfoxcolorado.com/weather/5_Day_Forecast.gif
mv fox.jpg fox_$(date +%Y%m%d-%H%M).jpg

wget -S -O 9news01.jpg http://www.9news.com/genthumb/genthumbwx.ashx?w=250&h=145&e=5&i=/weather/graphics/Today_Forecast.jpg
wget -S -O 9news02.jpg http://www.9news.com/genthumb/genthumbwx.ashx?w=250&h=145&e=5&i=/weather/graphics/Tonight_Forecast.jpg
wget -S -O 9news03.jpg http://www.9news.com/genthumb/genthumbwx.ashx?w=350&h=197&e=5&i=/weather/graphics/Planning_Forecast_popup.jpg
mv 9news01.jpg 9news01_$(date +%Y%m%d-%H%M).jpg
mv 9news02.jpg 9news02_$(date +%Y%m%d-%H%M).jpg
mv 9news03.jpg 9news03_$(date +%Y%m%d-%H%M).jpg

wget -S -O cbs4.jpg http://radar.cbslocal.com/kcnc/5day.jpg
mv cbs4.jpg cbs4_$(date +%Y%m%d-%H%M).jpg

wget -S -O denverchannel.jpg http://images.ibsys.com/den/images/weather/auto/kmgh_7day_640x480.jpg
mv denverchannel.jpg denverchannel_$(date +%Y%m%d-%H%M).jpg

wget -S -O weatherchannel.xml "http://xoap.weather.com/weather/local/USCO0105?cc=1&dayf=10&unit=s"
mv weatherchannel.xml weatherchannel_$(date +%Y%m%d-%H%M).xml

wget -S -O rmn.html http://www.rockymountainnews.com/weather/
mv rmn.html rmn_$(date +%Y%m%d-%H%M).html

wget -S -O dpo.html http://weathernow.denverpost.com/hw3.php
mv dpo.html dpo_$(date +%Y%m%d-%H%M).html

wget -S -O nws.html "http://forecast.weather.gov/MapClick.php?CityName=Denver&state=CO&site=BOU&textField1=39.768&textField2=-104.873"
mv nws.html nws_$(date +%Y%m%d-%H%M).html



// datadir/forecast_forecast.py
[220, 1, '2008-07-13']
[221, 2, '2008-07-13']
[222, 3, '2008-07-13']
[223, 4, '2008-07-13']
[224, 5, '2008-07-13']
[225, 6, '2008-07-13']
[226, 7, '2008-07-13']
[227, 8, '2008-07-13']
[228, 9, '2008-07-13']

// datadir/forecast_forecastitem.py
[2779, 0, None, 1, None, None, 220]
[2780, 1, None, 1, None, None, 220]
[2781, 2, None, 1, None, None, 220]
[2782, 3, None, 1, None, None, 220]
[2783, 4, None, 1, None, None, 220]
[2784, 5, None, 1, None, None, 220]
[2785, 0, None, -1, None, None, 220]
[2786, 1, None, -1, None, None, 220]
[2787, 2, None, -1, None, None, 220]
[2788, 3, None, -1, None, None, 220]
[2789, 4, None, -1, None, None, 220]
[2790, 5, None, -1, None, None, 220]
[2791, 0, None, 1, None, None, 221]
[2792, 1, None, 1, None, None, 221]
[2793, 2, None, 1, None, None, 221]
[2794, 3, None, 1, None, None, 221]
[2795, 4, None, 1, None, None, 221]
[2796, 0, None, -1, None, None, 221]
[2797, 1, None, -1, None, None, 221]
[2798, 2, None, -1, None, None, 221]
[2799, 3, None, -1, None, None, 221]
[2800, 0, None, 1, None, None, 222]
[2801, 1, None, 1, None, None, 222]
[2802, 2, None, 1, None, None, 222]
[2803, 3, None, 1, None, None, 222]
[2804, 4, None, 1, None, None, 222]
[2805, 5, None, 1, None, None, 222]
[2806, 6, None, 1, None, None, 222]
[2807, 0, None, -1, None, None, 222]
[2808, 1, None, -1, None, None, 222]
[2809, 2, None, -1, None, None, 222]
[2810, 3, None, -1, None, None, 222]
[2811, 4, None, -1, None, None, 222]
[2812, 5, None, -1, None, None, 222]
[2813, 0, None, 1, None, None, 223]
[2814, 1, None, 1, None, None, 223]
[2815, 2, None, 1, None, None, 223]
[2816, 3, None, 1, None, None, 223]
[2817, 4, None, 1, None, None, 223]
[2818, 5, None, 1, None, None, 223]
[2819, 6, None, 1, None, None, 223]
[2820, 7, None, 1, None, None, 223]
[2821, 8, None, 1, None, None, 223]
[2822, 9, None, 1, None, None, 223]
[2823, 0, None, -1, None, None, 223]
[2824, 1, None, -1, None, None, 223]
[2825, 2, None, -1, None, None, 223]
[2826, 3, None, -1, None, None, 223]
[2827, 4, None, -1, None, None, 223]
[2828, 5, None, -1, None, None, 223]
[2829, 6, None, -1, None, None, 223]
[2830, 7, None, -1, None, None, 223]
[2831, 8, None, -1, None, None, 223]
[2832, 9, None, -1, None, None, 223]
[2833, 0, None, 1, None, None, 224]
[2834, 1, None, 1, None, None, 224]
[2835, 2, None, 1, None, None, 224]
[2836, 3, None, 1, None, None, 224]
[2837, 4, None, 1, None, None, 224]
[2838, 0, None, -1, None, None, 224]
[2839, 1, None, -1, None, None, 224]
[2840, 2, None, -1, None, None, 224]
[2841, 3, None, -1, None, None, 224]
[2842, 4, None, -1, None, None, 224]
[2843, 0, None, 1, None, None, 225]
[2844, 1, None, 1, None, None, 225]
[2845, 2, None, 1, None, None, 225]
[2846, 3, None, 1, None, None, 225]
[2847, 4, None, 1, None, None, 225]
[2848, 5, None, 1, None, None, 225]
[2849, 6, None, 1, None, None, 225]
[2850, 0, None, -1, None, None, 225]
[2851, 1, None, -1, None, None, 225]
[2852, 2, None, -1, None, None, 225]
[2853, 3, None, -1, None, None, 225]
[2854, 4, None, -1, None, None, 225]
[2855, 5, None, -1, None, None, 225]
[2856, 0, None, 1, None, None, 226]
[2857, 1, None, 1, None, None, 226]
[2858, 2, None, 1, None, None, 226]
[2859, 3, None, 1, None, None, 226]
[2860, 4, None, 1, None, None, 226]
[2861, 5, None, 1, None, None, 226]
[2862, 6, None, 1, None, None, 226]
[2863, 0, None, -1, None, None, 226]
[2864, 1, None, -1, None, None, 226]
[2865, 2, None, -1, None, None, 226]
[2866, 3, None, -1, None, None, 226]
[2867, 4, None, -1, None, None, 226]
[2868, 5, None, -1, None, None, 226]
[2869, 6, None, -1, None, None, 226]
[2870, 0, None, 1, None, None, 227]
[2871, 1, None, 1, None, None, 227]
[2872, 2, None, 1, None, None, 227]
[2873, 3, None, 1, None, None, 227]
[2874, 4, None, 1, None, None, 227]
[2875, 0, None, -1, None, None, 227]
[2876, 1, None, -1, None, None, 227]
[2877, 2, None, -1, None, None, 227]
[2878, 3, None, -1, None, None, 227]
[2879, 0, None, 1, None, None, 228]
[2880, 1, None, 1, None, None, 228]
[2881, 2, None, 1, None, None, 228]
[2882, 3, None, 1, None, None, 228]
[2883, 4, None, 1, None, None, 228]
[2884, 5, None, 1, None, None, 228]
[2885, 6, None, 1, None, None, 228]
[2886, 0, None, -1, None, None, 228]
[2887, 1, None, -1, None, None, 228]
[2888, 2, None, -1, None, None, 228]
[2889, 3, None, -1, None, None, 228]
[2890, 4, None, -1, None, None, 228]
[2891, 5, None, -1, None, None, 228]
[2892, 6, None, -1, None, None, 228]
