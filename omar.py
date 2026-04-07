from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
css = """


@config(css_style=css)
def app():
    put_image('https://th.bing.com/th/id/OIP.RExrYRUsYqUKSMTByXaR2QHaHa?w=133h=180&c=7&r=0&o=7&pid=1.7&rm=3' ,width='1000px',height='200px')
    put_html("""
<h3 id='h3'>تطبيق القران الكريم </h3>
     <p id='para' >اهلا وسهلا بكم في تطبيقنا الجديد لحفظ القران الكريم</p>        
    <ul>
    <li>حفظ القران الكريم</li>
<><>

        <li>جميع سور القران الكريم بصوت الشيخ ماهر المعيقلي</li>
    </ul> 
            
    <details id= 'y'>
    <summary>سوره الفاتحه </summary>
    
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/001.mp3" type="audio/mp3">        
             </audio> 
             </details>
    <details id= 'y'> 
              <summary>سوره البقره </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/002.mp3" type="audio/mp3">        
             </audio>
             </details>
    <details id= 'y'>
              <summary>سوره ال عمران </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/003.mp3" type="audio/mp3">        
    </audio>
             </details>
            
            
   <details id= 'y'>
               <summary>سوره النساء</summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/004.mp3" type="audio/mp3">                
    </audio>
             </details>        
   
    <details id= 'y'>
              <summary>سوره المائده </summary>        
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/005.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <details id= 'y'>
             <summary>سوره الانعام</summary> 
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/006.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <details id= 'y'>
              <summary>سوره الاعراف </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/007.mp3" type="audio/mp3">        
    </audio>
             </details>
    <details id= 'y'>
             <summary>سوره الانفال </summary> 
      <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/008.mp3" type="audio/mp3">        
    </audio>     
             </details>      
    <details id= 'y'>
<summary>سوره التوبه </summary> 
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/009.mp3" type="audio/mp3">        
    </audio>    
             </details>                                                       
    <details id= 'y'>
             <summary>سوره يونس </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/010.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره هود </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/011.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره يوسف </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/012.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الرعد </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/013.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
              <summary>سوره ابراهيم </summary>
    <audio controls>
            
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/014.mp3" type="audio/mp3">        
    </audio>        
             </details>  
    <details id= 'y'>
             <summary>سوره الحجر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/015.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
              <summary>سوره النحل </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/016.mp3" type="audio/mp3">        
    </audio>    
             </details>      
   <details id= 'y'>
             <summary>سوره الاسراء </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/017.mp3" type="audio/mp3">        
    </audio>    
              </details>      
    <details id= 'y'>
             <summary>سوره الكهف </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/018.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره مريم </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/019.mp3" type="audio/mp3">        
    </audio>          
    </details>
    <details id= 'y'>
             <summary>سوره طه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/020.mp3" type="audio/mp3">        
    </audio>          
    </details>
    <details id= 'y'>
             <summary>سوره الانبياء</summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/021.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الحج </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/022.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره الؤمنون </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/023.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره النور </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/024.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الفرقان </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/025.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الشعراء </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/026.mp3" type="audio/mp3">        
    </audio>          
    </details>
    <details id= 'y'>
             <summary>سوره النمل </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/027.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره القصص </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/028.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره العنكبوت </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/029.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الروم </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/030.mp3" type="audio/mp3">        
    </audio>
             </details>          
    <details id= 'y'>
             <summary>سوره لقمان</summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/031.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره السجده </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/032.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الاحزاب </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/033.mp3" type="audio/mp3">        
   
    </audio> 
             </details>
    <details id= 'y'>         
             <summary>سوره سبأ </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/034.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره فاطر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/035.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره يس </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/036.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الصافات </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/037.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره ص </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/038.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره الزمر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/039.mp3" type="audio/mp3">        
    </audio> 
             </details>         
    <details id= 'y'>
             <summary>سوره غافر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/040.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره فصلت </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/041.mp3" type="audio/mp3">        
    </audio>     
             </details>     
    <details id= 'y'>
             <summary>سوره الشورى </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/042.mp3" type="audio/mp3">        
    </audio>  
   
             </details>        
    <details id= 'y'>
             <summary>سوره الزخرف </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/043.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الدخان </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/044.mp3" type="audio/mp3">        
    </audio>    
             </details>      
    <details id= 'y'>
             <summary>سوره الجاثيه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/045.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الاحقاف </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/046.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره محمد </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/047.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الفتح </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/048.mp3" type="audio/mp3">        
    </audio> 
    </details>           
                  
    <details id= 'y'>
             <summary>سوره الحجرات </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/049.mp3" type="audio/mp3">        
    </audio>       
             </details>   
           
    <details id= 'y'>
             <summary>سوره ق </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/050.mp3" type="audio/mp3">        
    </audio>  
             </details>        
    <details id= 'y'>
             <summary>سوره الذاريات </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/051.mp3" type="audio/mp3">        
    </audio>   
             </details>       
    <details id= 'y'>
             <summary>سوره الطور </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/052.mp3" type="audio/mp3">        
    </audio> 
             </details>
    <details id= 'y'>
             <summary>سوره النجم </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/053.mp3" type="audio/mp3">        
    </audio> 
             </details>   
     <details id= 'y'>
             <summary>سوره القمر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/054.mp3" type="audio/mp3">        
    </audio> 
             </details>  
     <details id= 'y'>
             <summary>سوره الرحمن </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/055.mp3" type="audio/mp3">        
    </audio> 
             </details>  
     <details id= 'y'>
             <summary>سوره الواقعه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/056.mp3" type="audio/mp3">        
    </audio> 
             </details>
     <details id= 'y'>
             <summary>سوره الحديد </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/057.mp3" type="audio/mp3">        
    </audio> 
             </details> 
     <details id= 'y'>
             <summary>سوره المجادله </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/058.mp3" type="audio/mp3">        
    </audio> 
             </details>  
         <details id= 'y'>
             <summary>سوره الحشر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/059.mp3" type="audio/mp3">        
    </audio> 
             </details> 
           <details id= 'y'>
             <summary>سوره الممتحنه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/060.mp3" type="audio/mp3">        
    </audio> 
             </details> 
          <details id= 'y'>
             <summary>سوره الصف </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/061.mp3" type="audio/mp3">        
    </audio> 
             </details> 
            <details id= 'y'>
             <summary>سوره الجمعه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/062.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المنافقون </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/063.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التغابن </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/064.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الطلاق </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/065.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التحريم </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/066.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الملك </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/067.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القلم </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/068.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الحاقه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/069.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المعارج </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/070.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره نوح </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/071.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الجن </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/072.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المزمل </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/073.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المدثر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/074.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القيامه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/075.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الانسان </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/076.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المرسلات </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/077.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره النبأ </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/078.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره النازعات </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/079.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره عبس </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/080.mp3" type="audio/mp3">        
    </audio> 
             </details>                                               
             <details id= 'y'>
             <summary>سوره التكوير </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/081.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الانفطار </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/082.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المطففين </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/083.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الانشقاق </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/084.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره البروج </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/085.mp3" type="audio/mp3">        
    </audio> 
             </details> <details id= 'y'>
             <summary>سوره الطارق </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/086.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الاعلى </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/087.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الغاشيه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/088.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الفجر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/089.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره البلد </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/090.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الشمس </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/091.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الليل </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/092.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الضحي </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/093.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الشرح </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/094.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التين </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/095.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره العلق </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/096.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القدر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/097.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره البينه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/098.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الزلزله </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/099.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره العاديات </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/100.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره القارعه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/101.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره التكاثر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/102.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره العصر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/103.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الهمزه </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/104.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الفيل </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/105.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره قريش </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/106.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الماعون </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/107.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الكوثر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/108.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الكافرون </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/109.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره النصر </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/110.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره المسد </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/111.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الاخلاص </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/112.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الفلق </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/113.mp3" type="audio/mp3">        
    </audio> 
             </details> 
             <details id= 'y'>
             <summary>سوره الناس </summary>
    <audio controls>
     <source src="https://download.ourquraan.com/Maher_Al-Muaiqly/114.mp3" type="audio/mp3">        
    </audio> """)
   
                            
.style('direction:rtl; text-align:right;')
    put_html("<hr id= 'r'>")
    put_text("جميع الحقوق محفوظه للمطو @ عمر صابر")
start_server(app , port=34345 , debug=True)


