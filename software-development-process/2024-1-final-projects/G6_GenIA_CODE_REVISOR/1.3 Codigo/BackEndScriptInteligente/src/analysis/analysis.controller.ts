import {
  Controller,
  Get,
  Post,
  Body,
  Param,
  Put,
  Delete,
  UseGuards,
  Req,
  UnauthorizedException,
} from '@nestjs/common';
import { AnalysisService } from './analysis.service';
import { Analysis } from '@prisma/client';
import {
  ApiTags,
  ApiOperation,
  ApiResponse,
  ApiParam,
  ApiBody,
} from '@nestjs/swagger';
import { JwtAuthGuard } from 'src/auth/local-auth.guard';

@ApiTags('analyses')
@Controller('analyses')
export class AnalysisController {
  constructor(private readonly analysisService: AnalysisService) {}

  @Post()
  @ApiOperation({ summary: 'Create a new analysis' })
  @ApiResponse({
    status: 201,
    description: 'The analysis has been successfully created.',
  })
  @ApiBody({
    schema: {
      example: {
        scriptId: 1,
        initialPrompt: 'Check for errors in the script.',
      },
    },
  })
  async createAnalysis(
    @Body() body: { scriptId: number; initialPrompt: string },
  ): Promise<Analysis> {
    return this.analysisService.createAnalysis(
      body.scriptId,
      body.initialPrompt,
    );
  }

  @UseGuards(JwtAuthGuard)
  @Get('user/:userId')
  async getUserAnalyses(@Param('userId') userId: string, @Req() req) {
    if (req.user.id !== parseInt(userId, 10)) {
      throw new UnauthorizedException();
    }
    return this.analysisService.getAnalysesByUser(userId);
  }

  @Put(':id')
  @ApiOperation({ summary: 'Update analysis by ID' })
  @ApiResponse({
    status: 200,
    description: 'The analysis has been successfully updated.',
  })
  @ApiParam({ name: 'id', required: true, description: 'Analysis ID' })
  @ApiBody({ schema: { example: { result: 'Updated analysis result' } } })
  async updateAnalysis(
    @Param('id') id: string,
    @Body() analysisData: { result?: string },
  ): Promise<Analysis> {
    return this.analysisService.updateAnalysis(Number(id), analysisData);
  }

  @Delete(':id')
  @ApiOperation({ summary: 'Delete analysis by ID' })
  @ApiResponse({
    status: 200,
    description: 'The analysis has been successfully deleted.',
  })
  @ApiParam({ name: 'id', required: true, description: 'Analysis ID' })
  async deleteAnalysis(@Param('id') id: string): Promise<Analysis> {
    return this.analysisService.deleteAnalysis(Number(id));
  }
}
