import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {BlogsApiService} from './blogs/blogs-api.service';
import {HttpClientModule} from '@angular/common/http';
import {BlogComponent} from "./blogs/blog.component";
import {BlogListComponent} from "./blogs/blog-list.component";
import { routing, appRoutingProviders } from "./app-routing.module";
import {AddBlogomponent} from "./blogs/add-blog.component";


@NgModule({
  declarations: [
    AppComponent,
    BlogComponent,
    BlogListComponent,
    AddBlogomponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    routing
  ],
  providers: [BlogsApiService, appRoutingProviders],
  bootstrap: [AppComponent]
})
export class AppModule { }
