import { Component, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Front';

  constructor(private http: HttpClient){}

  apiResponse: any;

  onSubmit(data:any) {
    // const data2 = {
    //   Pclass: parseInt(data.Pclass),
    //   Sex: parseInt(data.Sex),
    //   Age: parseFloat(data.Age),
    //   SibSp: parseInt(data.SibSp),
    //   eParch: parseInt(data.eParch),
    // };

    
    
    console.warn(data);
    return this.http.post('http://localhost:8000/predict', data).subscribe(response => {
      this.apiResponse = response;
      console.log(response);
    });
  }
  
}

@Injectable()
export class CorsInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const corsReq = req.clone({ headers: req.headers.set('Access-Control-Allow-Origin', '*')
    .set('Access-Control-Allow-Headers', 'Content-Type, Accept'), });
    return next.handle(corsReq);
  }
}