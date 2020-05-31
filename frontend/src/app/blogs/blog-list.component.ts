import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {Blog} from "../models/blog";
import {BlogsApiService} from "./blogs-api.service";

@Component({
  selector: 'blog-list',
  templateUrl: './blog-list.component.html',
  styleUrls: []
})
export class BlogListComponent implements OnInit, OnDestroy {
  blogsListSubs: Subscription;
  blogsList: Blog[];

  constructor(private blogsApi: BlogsApiService) {
  }

  ngOnInit() {
    this.blogsListSubs = this.blogsApi
      .getBlogs()
      .subscribe(res => {
          console.log(res);
          this.blogsList = res;
        },
        console.error
      );
    // this.blogsList = this.blogsApi.getBlogs();
  }

  ngOnDestroy() {
    // this.blogsListSubs.unsubscribe();
  }
}