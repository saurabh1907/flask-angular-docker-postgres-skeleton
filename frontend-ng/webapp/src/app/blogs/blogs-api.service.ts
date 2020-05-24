import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import {catchError} from 'rxjs/operators';
import {API_URL} from '../env';
import {Blog} from './blog.model';


@Injectable()
export class BlogsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  // getBlogs(): Observable<Blog[]> {
  //   return this.http
  //     .get<Blog[]>(`${API_URL}/blogs`)
  //     .pipe(catchError(this.errorHandler))
  // }

  getBlogs() {
    let blogs = new Array();
    blogs.push(new Blog('1','first blog',1));
    blogs.push(new Blog('2','second blog',2));
    blogs.push(new Blog('2','third blog',3));
    return blogs;
  }

    getBlog(id) {
    return new Blog('2','third blog',3);
  }
   saveBlog(blog: Blog): Observable<any> {
    return this.http
      .post(`${API_URL}/blogs`, blog);
  }

   errorHandler(error: HttpErrorResponse) {
        return Observable.throw(error.message || "server error.");
    }
}
