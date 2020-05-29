import {Component} from '@angular/core';
import {Router} from "@angular/router";
import {BlogsApiService} from "./blogs-api.service";
import {Blog} from "../models/blog";

@Component({
  selector: 'add-blog',
  templateUrl: './add-blog.component.html',
  styleUrls: []
})
export class AddBlogomponent {
  blog:Blog = new Blog()

  constructor(private blogApi: BlogsApiService, private router: Router) { }

  updateTitle(event: any) {
    this.blog.title = event.target.value;
  }

  updateDescription(event: any) {
    this.blog.description = event.target.value;
  }

  saveBlog() {
    console.log('saving');
    console.log(this.blog.title);
    // this.blogApi
    //   .saveBlog(this.blog)
    //   .subscribe(
    //     () => this.router.navigate(['/']),
    //     error => alert(error.message)
    //   );
  }
}
