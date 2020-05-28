import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {BlogsApiService} from './blogs/blogs-api.service';
import {Blog} from './blogs/blog.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: []
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';

  constructor() {
  }

  ngOnInit() {

  }

  ngOnDestroy() {

  }
}
