import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { ActivatedRoute } from "@angular/router";
import {BlogService} from "../service/blog.service";
import {Blog} from "../models/blog";

@Component({
  selector: "app-view-blog",
  templateUrl: "./view-blog.component.html",
  styleUrls: []
})
export class ViewBlogComponent implements OnInit {
  loading: boolean = true;
  blog: Blog;
  editable: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private blogService: BlogService
  ) {}

  ngOnInit() {
    this.getBlog();
    console.log(this.blog);
  }

  public deleteBlog() {
    const id = this.route.snapshot.paramMap.get('id');
    this.blogService.deleteBlog(id).subscribe(res => {
      console.log('Deleted Blog' + id);
      this.router.navigate(['/home']);
    });
  }

  public editableToggle() {
    this.editable = !this.editable;
  }

  private getBlog(): void {
    const id = this.route.snapshot.paramMap.get('id');
    console.log('id: ' + id);

    this.blogService.getBlog(id).subscribe(blog => {
      console.log('blog: ' + JSON.stringify(blog));
      this.blog = blog;
      this.loading = false;
    });
  }
}
