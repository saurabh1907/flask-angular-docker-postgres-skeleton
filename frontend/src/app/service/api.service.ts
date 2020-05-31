import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

import { environment } from '../../environments/environment';
import {HttpHeaders} from '@angular/common/http';
const API_BASE_URL = environment.api.base;

@Injectable({
  providedIn: 'root' // TODO: figure out how to inject service instead of being at root of app
})
export class ApiService {
  constructor(private http: Http) {}
  headers = new HttpHeaders().set('Content-Type', 'application/json');

  public get(requestUri: string): Observable<any> {
    return this.http
      .get(API_BASE_URL + requestUri, {headers: this.headers})
      .pipe(
        map(response => {
          const json = response.json();
          return json;
        })
      )
      .pipe(catchError(this.handleError));
  }

  public post(requestUri: string, data: any): Observable<any> {
    return this.http
      .post(API_BASE_URL + requestUri, data)
      .pipe(catchError(this.handleError));
  }

   public put(requestUri: string, data: any): Observable<any> {
    return this.http
      .put(API_BASE_URL + requestUri, data)
      .pipe(catchError(this.handleError));
  }

  public delete(requestUri: string) {
    return this.http
      .delete(API_BASE_URL + requestUri)
      .pipe(catchError(this.handleError));
  }


  private handleError(error: Response | any) {
    console.error('ApiService::handleError', error);
    return throwError(error);
  }

}
