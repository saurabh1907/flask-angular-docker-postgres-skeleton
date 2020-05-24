import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {Blog} from "./blog.model";
import {BlogsApiService} from "./blogs-api.service";

@Component({
  selector: 'blog',
  templateUrl: './blog.component.html',
  styleUrls: []
})
export class BlogComponent implements OnInit, OnDestroy {
  blogSubs: Subscription;
  blog: Blog;

  constructor(private blogsApi: BlogsApiService) {
  }

  ngOnInit() {
    // this.blogsListSubs = this.blogsApi
    //   .getBlogs()
    //   .subscribe(res => {
    //       this.blogsList = res;
    //     },
    //     console.error
    //   );
    this.blog= this.blogsApi.getBlog(1);
  }

  ngOnDestroy() {
    this.blogSubs.unsubscribe();
  }
}
