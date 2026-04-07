from pywebio import start_server
from pywebio.output import put_markdown, put_success, put_warning, put_text ,put_image ,put_html
from pywebio.session import run_js
import time
from pywebio import *
from pywebio.input import *
from pywebio import config
from pywebio.output import *


def main():
    ts = int(time.time())

    run_js(f"""
        var existing = document.querySelectorAll("link[rel*='icon']");
        existing.forEach(function(el) {{ el.parentNode.removeChild(el); }});

        var link = document.createElement('link');
        link.rel = 'shortcut icon';
        link.type = 'image/png';
        link.href = 'https://i.pinimg.com/736x/8c/e7/2b/8ce72b30497eafdadba42889cf04255b.jpg?v={ts}';
        document.head.appendChild(link);
        document.title = 'القران الكريم';

        console.log(' تم تعيين الأيقونة:', link.href);
    """)
    put_image('https://th.bing.com/th/id/OIP.RExrYRUsYqUKSMTByXaR2QHaHa?w=133h=180&c=7&r=0&o=7&pid=1.7&rm=3' ,width='1000px',height='200px')
    put_html("""
        <h3 id='h3'> تطبيق القران الكريم </h3>
    <p id=para>اهلا وسهلا بكم في تطبيقنا الجديد لحفظ القران الكريم</p>         
    <ul>
        <li id= 't'>حفظ القران الكريم</li>
        <li id= 't'>جميع سور القران الكريم</li>
        <li id= 't'>جميع سور القران الكريم بصوت الشيخ ماهر المعيقلي</li>
    </ul> 
            
    <details id= 'y'>
    <summary>سوره الفاتحه </summary>
    
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/001.mp3" type="audio/mp3">        
             </audio> 
             </details>
    <details id= 'y'> 
              <summary>سوره البقره </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/002.mp3" type="audio/mp3">        
             </audio>
             </details>
    <details id= 'y'>
              <summary>سوره ال عمران </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/003.mp3" type="audio/mp3">        
    </audio>
             </details>
            
            
   <details id= 'y'>
               <summary>سوره النساء</summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/004.mp3" type="audio/mp3">                
    </audio>
             </details>        
   
    <details id= 'y'>
              <summary>سوره المائده </summary>        
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/005.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <details id= 'y'>
             <summary>سوره الانعام</summary> 
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/006.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <details id= 'y'>
              <summary>سوره الاعراف </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/007.mp3" type="audio/mp3">        
    </audio>
             </details>
    <details id= 'y'>
             <summary>سوره الانفال </summary> 
      <audio controls>
     <source src="https://server12.mp3quran.net/maher/008.mp3" type="audio/mp3">        
    </audio>     
             </details>      
    <details id= 'y'>
<summary>سوره التوبه </summary> 
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/009.mp3" type="audio/mp3">        
    </audio>    
             </details>                                                       
    <details id= 'y'>
             <summary>سوره يونس </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/010.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره هود </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/011.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره يوسف </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/012.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الرعد </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/013.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    
    <details id= 'y'>
              <summary>سوره ابراهيم </summary>
     <audio controls>       
     <source src="https://server12.mp3quran.net/maher/014.mp3" type="audio/mp3">        
    </audio>        
             </details>  
    <details id= 'y'>
             <summary>سوره الحجر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/015.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
              <summary>سوره النحل </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/016.mp3" type="audio/mp3">        
    </audio>    
             </details>      
   <details id= 'y'>
             <summary>سوره الاسراء </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/017.mp3" type="audio/mp3">        
    </audio>    
              </details>      
    <details id= 'y'>
             <summary>سوره الكهف </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/018.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره مريم </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/019.mp3" type="audio/mp3">        
    </audio>          
    </details>
    <details id= 'y'>
             <summary>سوره طه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/020.mp3" type="audio/mp3">        
    </audio>          
    </details>
    <details id= 'y'>
             <summary>سوره الانبياء</summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/021.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الحج </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/022.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره الؤمنون </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/023.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره النور </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/024.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الفرقان </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/025.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الشعراء </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/026.mp3" type="audio/mp3">        
    </audio>          
    </details>
    <details id= 'y'>
             <summary>سوره النمل </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/027.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره القصص </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/028.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره العنكبوت </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/029.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الروم </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/030.mp3" type="audio/mp3">        
    </audio>
             </details>          
    <details id= 'y'>
             <summary>سوره لقمان</summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/031.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره السجده </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/032.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الاحزاب </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/033.mp3" type="audio/mp3">        
   
    </audio> 
             </details>
    <details id= 'y'>         
             <summary>سوره سبأ </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/033.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره فاطر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/035.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره يس </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/036.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الصافات </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/037.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره ص </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/038.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره الزمر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/039.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره غافر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/040.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره فصلت </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/041.mp3" type="audio/mp3">        
    </audio>     
             </details>     
    <details id= 'y'>
             <summary>سوره الشورى </summary>
    <audio controls>
<source src="https://server12.mp3quran.net/maher/042.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الزخرف </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/043.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الدخان </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/044.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره الجاثيه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/045.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الاحقاف </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/046.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره محمد </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/047.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الفتح </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/048.mp3" type="audio/mp3">        
    </audio> 
    </details>           
                  
    <details id= 'y'>
             <summary>سوره الحجرات </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/049.mp3" type="audio/mp3">        
    </audio>       
             </details>   
           
    <details id= 'y'>
             <summary>سوره ق </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/050.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الذاريات </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/051.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الطور </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/052.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <details id= 'y'>
             <summary>سوره النجم </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/053.mp3" type="audio/mp3">        
    </audio> 
             </details>   
     <details id= 'y'>
             <summary>سوره القمر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/054.mp3" type="audio/mp3">        
    </audio> 
             </details>  
     <details id= 'y'>
             <summary>سوره الرحمن </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/055.mp3" type="audio/mp3">        
    </audio> 
             </details>  
     <details id= 'y'>
             <summary>سوره الواقعه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/056.mp3" type="audio/mp3">        
    </audio> 
             </details>
     <details id= 'y'>
             <summary>سوره الحديد </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/057.mp3" type="audio/mp3">        
    </audio> 
             </details> 
     <details id= 'y'>
             <summary>سوره المجادله </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/058.mp3" type="audio/mp3">        
    </audio> 
             </details>  
         <details id= 'y'>
             <summary>سوره الحشر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/059.mp3" type="audio/mp3">        
    </audio> 
             </details> 
           <details id= 'y'>
             <summary>سوره الممتحنه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/060.mp3" type="audio/mp3">        
    </audio> 
             </details> 
          <details id= 'y'>
             <summary>سوره الصف </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/061.mp3" type="audio/mp3">        
    </audio> 
             </details> 
            <details id= 'y'>
             <summary>سوره الجمعه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/062.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المنافقون </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/063.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التغابن </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/064.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الطلاق </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/065.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التحريم </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/066.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الملك </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/067.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القلم </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/068.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الحاقه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/069.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المعارج </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/070.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره نوح </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/071.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الجن </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/072.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المزمل </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/073.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المدثر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/074.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القيامه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/075.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الانسان </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/076.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المرسلات </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/077.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره النبأ </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/078.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره النازعات </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/079.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره عبس </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/080.mp3" type="audio/mp3">        
    </audio> 
             </details>                                               
             <details id= 'y'>
             <summary>سوره التكوير </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/081.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الانفطار </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/082.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المطففين </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/083.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الانشقاق </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/084.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره البروج </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/085.mp3" type="audio/mp3">        
    </audio> 
             </details> <details id= 'y'>
             <summary>سوره الطارق </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/086.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الاعلى </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/087.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الغاشيه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/088.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الفجر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/089.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره البلد </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/090.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الشمس </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/091.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الليل </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/092.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details>
             <summary>سوره الضحي </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/093.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الشرح </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/094.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التين </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/095.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره العلق </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/096.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القدر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/097.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره البينه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/098.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الزلزله </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/099.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره العاديات </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/100.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القارعه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/101.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التكاثر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/102.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره العصر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/103.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الهمزه </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/104.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الفيل </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/105.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره قريش </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/106.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الماعون </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/107.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الكوثر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/108.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الكافرون </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/109.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره النصر </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/110.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المسد </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/111.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الاخلاص </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/112.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الفلق </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/113.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الناس </summary>
    <audio controls>
     <source src="https://server12.mp3quran.net/maher/114.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <hr id='o'>
   <p>جميع الحقوق محفوظه للمطو @ عمر صابر</p>          
   
                              
""").style('direction:rtl; text-align:right;')



if __name__ == "__main__":
    start_server(main, port=8081, open_webbrowser=True)